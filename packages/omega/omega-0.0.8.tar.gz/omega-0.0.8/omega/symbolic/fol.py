"""First-order wrapper for BDDs."""
# other places where relevant functions exist:
#   dd.mdd
#   omega.logic.bitvector
#   omega.symbolic.enumeration
#
# examples/interleaving
# symbolic_transducers
# simulate
import logging

try:
    from dd import cudd as _bdd
except ImportError:
    from dd import bdd as _bdd

from omega.logic import bitvector as bv
from omega.logic import syntax as stx
from omega.symbolic import bdd as sym_bdd
from omega.symbolic import enumeration as enum
from omega.symbolic import symbolic


log = logging.getLogger(__name__)


class Context(object):
    """First-order interface to a binary decision diagram."""

    def __init__(self):
        """Instantiate first-order context."""
        self.vars = dict()
        self.bdd = _bdd.BDD()

    def add_vars(self, dvars):
        """Bitblast and add variables in `dvars`.

        These variables can have integer or Boolean type hints.
        Type hints are used to choose a refinement of
        integers by finitely many bits.

        No type predicates managed here:
        This is an untyped logic!

        Priming is not reasoned about here.
        Priming is the responsibility of higher levels.
        """
        # should be fresh
        common = set(dvars).intersection(self.vars)
        assert not common, common
        t = bv.bitblast_table(dvars)
        self.vars.update(t)
        bits = bv.bit_table(t, t)
        for bit in bits:
            self.bdd.add_var(bit)

    def support(self, u):
        """Return FOL variables that `u` depends on."""
        supp = self.bdd.support(u)
        bit2int = bv.map_bits_to_integers(self.vars)
        return set(map(bit2int.__getitem__, supp))

    def replace(self, u, vars_to_new):
        """Return substitution of var names by values or vars.

        @param vars_to_new: `dict` that maps each var name to
            a var (as `str`), or to a value (as `bool` or `int`).
        """
        if not vars_to_new:
            return u
        assert vars_to_new, vars_to_new
        for k in vars_to_new:
            try:
                vars_to_new[k] + 'str'
                rename = True
            except TypeError:
                rename = False
            break
        if rename:
            bit_rename = _refine_renaming(vars_to_new, self.vars)
            return self.bdd.rename(u, bit_rename)
        else:
            bit_values = _refine_assignment(vars_to_new, self.vars)
            return self.bdd.cofactor(u, bit_values)

    def replace_with_bdd(self, u, var_subs):
        """Substitute Boolean-valued variables with BDD nodes."""
        # distinct from `replace` due to restriction to Boolean
        return self.bdd.compose(u, var_subs)

    def forall(self, qvars, u):
        """Universally quantify `qvars` in `u`."""
        return ~self.exist(qvars, ~u)

    def exist(self, qvars, u):
        """Existentially quantify `qvars` in `u`."""
        qbits = bv.bit_table(qvars, self.vars)
        return self.bdd.exist(qbits, u)

    def pick(self, u, full, care_vars):
        """Return a satisfying assignment, or `None`."""
        try:
            return next(self.sat_iter(u, full, care_vars))
        except StopIteration:
            return None

    def sat_iter(self, u, full, care_vars):
        """Return generator of first-order satisfying assignments."""
        care_bits = bv.bit_table(care_vars, self.vars)
        for bit_assignment in self.bdd.sat_iter(
                u, full=full, care_bits=care_bits):
            d = next(enum._bitfields_to_int_iter(
                bit_assignment, self.vars))
            yield d

    def add_expr(self, e):
        """Add first-order formula."""
        s = bv.bitblast(e, self.vars)
        return sym_bdd.add_expr(s, self.bdd)

    def apply(self, op, u, v=None, w=None):
        """Apply operator `op` on operands `u, v, w`."""
        return self.bdd.apply(op, u, v, w)


def reorder(dvars, fol):
    """Shift integers up in the variable order of `fol.bdd`."""
    bdd = fol.bdd
    for var, d in dvars.iteritems():
        level = d['level']
        dv = fol.vars[var]
        var_type = dv['type']
        if var_type == 'bool':
            bitnames = [var]
        else:
            assert var_type in ('int', 'saturating', 'modwrap')
            bitnames = dv['bitnames']
        # print('Shifting bits {bitnames} to '
        #       'level {level}'.format(
        #         level=level,
        #         bitnames=bitnames))
        # assert each bit goes up in level
        for bit in bitnames:
            old_level = bdd.level_of_var(bit)
            assert old_level >= level, (old_level, level)
        # shift to levels wanted
        order = [bdd.var_at_level(i)
                 for i in xrange(len(bdd.vars))]
        below = order[:level]
        above = order[level:]
        above = [v for v in above if v not in bitnames]
        new_order = below + bitnames + above
        dorder = {var: i for i, var in enumerate(new_order)}
        _bdd.reorder(bdd, dorder)
        order = [bdd.var_at_level(i)
                 for i in xrange(len(bdd.vars))]
        assert order == new_order, (order, new_order)


def _refine_assignment(fol_values, table):
    """Return assignment to bits, from FOL assignment."""
    bit_values = dict()
    for var, value in fol_values.iteritems():
        assert var in table, var
        if table[var]['type'] == 'bool':
            bit_values[var] = value
            continue
        d = _int_to_bit_assignment(var, value, table)
        bit_values.update(d)
    return bit_values


def _refine_renaming(fol_rename, table):
    """Return renaming of bits, from renaming of FOL vars."""
    bit_rename = dict()
    for old, new in fol_rename.iteritems():
        old_d = table[old]
        new_d = table[new]
        old_type = old_d['type']
        new_type = new_d['type']
        assert old_type == new_type, (old_type, new_type)
        if old_type == 'bool':
            bit_rename[old] = new
            continue
        assert old_type in ('int', 'saturating', 'modwrap')
        # int
        old_dom = old_d['dom']
        new_dom = new_d['dom']
        assert old_dom == new_dom, (old_dom, new_dom)
        old_bits = old_d['bitnames']
        new_bits = new_d['bitnames']
        assert len(old_bits) == len(new_bits), (
            old_bits, new_bits)
        # no overlap (otherwise use `compose`)
        common = set(old_bits).intersection(new_bits)
        assert not common, (
            common, old_bits, new_bits)
        # bit substitution
        # assume same bit numbering (index 0 is LSB)
        bit_rename.update(zip(old_bits, new_bits))
    return bit_rename


def _int_to_bit_assignment(var, value, table):
    """Return assignment to bits from assignment to integer."""
    assert var in table, var
    var_bits = bv.var_to_twos_complement(var, table)
    int_bits = bv.int_to_twos_complement(value)
    p, q = bv.equalize_width(var_bits, int_bits)
    values = dict()
    for u, v in zip(p, q):
        # primed ?
        if u.isdigit():
            assert u == v, (u, v)
        else:
            values[u] = bool(int(v))
    return values


def _prime_bits_of_integers(ints, t):
    """Return bit priming for integers in `x`."""
    bit_rename = dict()
    for i in ints:
        bits = t.vars[i]['bitnames']
        d = {k: stx.prime(k) for k in bits}
        bit_rename.update(d)
    return bit_rename


def closed_interval(var, a, b):
    """Return string `a <= var <= b`."""
    return (
        '({a} <= {var}) & '
        '({var} <= {b})').format(
            var=var, a=a, b=b)


def add_one_hot(var, a, b):
    """Return symbol table for one-hot encoding."""
    t = dict()
    for i in xrange(a, b):
        var = '{var}{i}'.format(var=var, i=i)
        d = dict(type='bool', owner='parameters', level=0)
        t[var] = d
    return t


def array_to_logic(a, counter, aut):
    """Return logic formula for Boolean array `a`.

    No array bounds produced.
    Instead, if `(counter < 0) or (counter >= len(a) - 1)`,
    then select `a[-1]`.
    Therefore, array bounds *must* be added separately.

    @param a: `list` of elements
    @param counter: name of index variable
    """
    bdd = aut.bdd
    r = a[-1]
    for i, x in enumerate(a[:-1]):
        s = '{counter} = {i}'.format(counter=counter, i=i)
        u = aut.add_expr(s)
        r = bdd.ite(u, x, r)
    return r


def multiplexer(a, bits, aut):
    """Return BDD node for selection of elements from `a`.

    The resulting expression is:

    ```
    ite(bits[-1], a[-1],
        ite(bits[-2], a[-2],
            ...
            ite(bits[1], a[1],
                ite(bits[0], a[0], FALSE)
    ```

    This shows that if i < j,
    then b[i] has lower priority than b[j].
    So, this is not exactly a multiplexer.
    """
    assert len(a) == len(bits), (a, bits)
    bdd = aut.bdd
    r = bdd.false
    for bit, x in zip(bits, a):
        g = aut.add_expr(bit)
        r = bdd.ite(g, x, r)
    return r
