"""Algorithms for generalized Streett and Rabin games.


References
==========

Roderick Bloem, Barbara Jobstmann, Nir Piterman,
Amir Pnueli, Yaniv Sa'ar
    "Synthesis of reactive(1) designs"
    Journal of Computer and System Sciences
    Vol.78, No.3, pp.911--938, 2012


Robert Konighofer
    "Debugging formal specifications with
    simplified counterstrategies"
    Master's thesis
    Inst. for Applied Information Processing and Communications,
    Graz University of Technology, 2009
"""
import logging
import copy
from omega.symbolic import fixpoint as fx
from omega.symbolic import symbolic


logger = logging.getLogger(__name__)


# TODO:
# - switch to `dd.autoref`


def solve_streett_game(aut, rank=1):
    """Return winning set and iterants for Streett(1) game.

    @param aut: compiled game with <>[] | []<> winning
    @type aut: `symbolic.Automaton`
    """
    assert rank == 1, 'only rank 1 supported for now'
    assert not aut.vars or aut.bdd.vars, (
        'first call `Automaton.build`')
    aut.assert_consistent(built=True)
    assert len(aut.win['<>[]']) > 0
    assert len(aut.win['[]<>']) > 0
    bdd = aut.bdd
    z = bdd.true
    zold = None
    while z != zold:
        zold = z
        xijk = list()
        yij = list()
        for goal in aut.win['[]<>']:
            y, yj, xjk = _attractor_under_assumptions(z, goal, aut)
            z = bdd.apply('and', z, y)
            xijk.append(xjk)
            yij.append(yj)
    return z, yij, xijk


def _attractor_under_assumptions(z, goal, aut):
    """Targeting `goal`, under unconditional assumptions."""
    bdd = aut.bdd
    env_action = aut.action['env'][0]
    sys_action = aut.action['sys'][0]
    xjk = list()
    yj = list()
    y = bdd.false
    yold = None
    cox_z = fx.ue_preimage(env_action, sys_action, z, aut)
    g = bdd.apply('and', goal, cox_z)
    while y != yold:
        yold = y
        cox_y = fx.ue_preimage(env_action, sys_action, y, aut)
        unless = bdd.apply('or', cox_y, g)
        xk = list()
        for safe in aut.win['<>[]']:
            x = fx.trap(env_action, sys_action,
                        safe, aut, unless=unless)
            xk.append(x)
            y = bdd.apply('or', y, x)
        yj.append(y)
        xjk.append(xk)
    return y, yj, xjk


def make_streett_transducer(z, yij, xijk, aut):
    """Return I/O `symbolic.Automaton` implementing strategy.

    An auxiliary variable `_goal` is added,
    to represent the counter of recurrence goals.
    """
    aut.assert_consistent(built=True)
    assert z != aut.bdd.false, 'empty winning set'
    # add goal counter var
    c = '_goal'
    dvars = copy.deepcopy(aut.vars)
    n_goals = len(aut.win['[]<>'])
    dvars[c] = dict(
        type='saturating',
        dom=(0, n_goals - 1),
        owner='sys')
    # compile transducer with refined shared BDD
    t = symbolic.Automaton()
    t.vars = dvars
    bdd = aut.bdd
    t.bdd = bdd
    t = t.build()
    env_init = aut.init['env'][0]
    sys_init = aut.init['sys'][0]
    env_action = aut.action['env'][0]
    sys_action = aut.action['sys'][0]
    holds = aut.win['<>[]']
    goals = aut.win['[]<>']
    # compute strategy from iterates
    # \rho_1: switch goals
    rho_1 = bdd.false
    for i, goal in enumerate(goals):
        ip = (i + 1) % len(goals)
        s = "({c} = {i}) & ({c}' = {ip})".format(c=c, i=i, ip=ip)
        u = t.add_expr(s)
        u = bdd.apply('and', u, goal)
        rho_1 = bdd.apply('or', u, rho_1)
    zp = bdd.rename(z, t.prime)
    rho_1 = bdd.apply('and', rho_1, zp)
    # \rho_2: descent in basin
    rho_2 = bdd.false
    for i, yj in enumerate(yij):
        s = "({c} = {i}) & ({c}' = {i})".format(c=c, i=i)
        count = t.add_expr(s)
        rho_2j = bdd.false
        basin = yj[0]
        for y in yj[1:]:
            next_basin = bdd.rename(basin, t.prime)
            rim = bdd.apply('diff', y, basin)
            u = bdd.apply('and', rim, next_basin)
            rho_2j = bdd.apply('or', rho_2j, u)
            basin = bdd.apply('or', basin, y)
        u = bdd.apply('and', rho_2j, count)
        rho_2 = bdd.apply('or', rho_2, u)
    # \rho_3: persistence holds
    rho_3 = bdd.false
    for i, xjk in enumerate(xijk):
        s = "({c} = {i}) & ({c}' = {i})".format(c=c, i=i)
        count = t.add_expr(s)
        rho_3j = bdd.false
        used = bdd.false
        for xk in xjk:
            assert len(xk) == len(holds), xk
            for x, hold in zip(xk, holds):
                next_wait = bdd.rename(x, t.prime)
                stay = bdd.apply('diff', x, used)
                used = bdd.apply('or', used, x)
                u = bdd.apply('and', stay, next_wait)
                u = bdd.apply('and', u, hold)
                rho_3j = bdd.apply('or', rho_3j, u)
        u = bdd.apply('and', rho_3j, count)
        rho_3 = bdd.apply('or', rho_3, u)
    # \rho
    u = bdd.apply('or', rho_1, rho_2)
    u = bdd.apply('or', rho_3, u)
    u = bdd.apply('and', sys_action, u)
    # counter `c` limits
    u = bdd.apply('and', t.action['sys'][0], u)
    if not aut.plus_one:
        u = bdd.apply('->', env_action, u)
    if aut.moore:
        u = bdd.forall(t.upvars, u)
    t.action['sys'] = [u]
    # initial condition for counter
    # (no closure taken for counter)
    s = '{c} = 0'.format(c=c)
    count = t.add_expr(s)
    win_set = z
    # \A init
    init = _all_init(env_init, sys_init, count, bdd)
    t.init['env'] = [init]
    init = bdd.apply('->', init, win_set)
    assert init == bdd.true, 'losing from some init states'
    return t


def solve_rabin_game(aut, rank=1):
    """Return winning set and iterants for Rabin(1) game.

    @param aut: compiled game with <>[] & []<> winning
    @type aut: `symbolic.Automaton`
    """
    assert rank == 1, 'only rank 1 supported for now'
    assert not aut.vars or aut.bdd.vars, (
        'first call `Automaton.build`')
    aut.assert_consistent(built=True)
    # TODO: can these assertions be removed elegantly ?
    assert len(aut.win['<>[]']) > 0
    assert len(aut.win['[]<>']) > 0
    bdd = aut.bdd
    z = bdd.false
    zold = None
    zk = list()
    yki = list()
    xkijr = list()
    while z != zold:
        zold = z
        xijr = list()
        yi = list()
        for hold in aut.win['<>[]']:
            y, xjr = _cycle_inside(zold, hold, aut)
            z = bdd.apply('or', z, y)
            xijr.append(xjr)
            yi.append(y)
        zk.append(z)
        yki.append(yi)
        xkijr.append(xijr)
    return zk, yki, xkijr


def _cycle_inside(z, hold, aut):
    """Cycling through goals, while staying in `hold`."""
    bdd = aut.bdd
    env_action = aut.action['env'][0]
    sys_action = aut.action['sys'][0]
    cox_z = fx.ue_preimage(env_action, sys_action,
                           z, aut)
    g = bdd.apply('or', cox_z, hold)
    y = bdd.true
    yold = None
    while y != yold:
        yold = y
        cox_y = fx.ue_preimage(env_action, sys_action,
                               y, aut)
        inside = bdd.apply('and', cox_y, g)
        xjr = list()
        for goal in aut.win['[]<>']:
            x, xr = _attractor_inside(inside, goal, aut)
            xjr.append(xr)
            y = bdd.apply('and', y, x)
    return y, xjr


def _attractor_inside(inside, goal, aut):
    bdd = aut.bdd
    env_action = aut.action['env'][0]
    sys_action = aut.action['sys'][0]
    xr = list()
    x = bdd.false
    xold = None
    while x != xold:
        xold = x
        cox_x = fx.ue_preimage(
            env_action, sys_action, x, aut,
            evars=aut.epvars)
        x = bdd.apply('or', cox_x, goal)
        x = bdd.apply('and', x, inside)
        x = bdd.apply('or', x, xold)
        xr.append(x)
    return x, xr


def make_rabin_transducer(zk, yki, xkijr, aut):
    """Return O/I transducer for Rabin(1) game."""
    aut.assert_consistent(built=True)
    win_set = zk[-1]
    assert win_set != aut.bdd.false, 'empty winning set'
    dvars = dict(aut.vars)
    n_holds = len(aut.win['<>[]'])
    n_goals = len(aut.win['[]<>'])
    # add transducer memory as two indices:
    # - `w`: persistence hold index
    # - `c`: recurrence goal index
    w = '_hold'
    c = '_goal'
    n_w = n_holds - 1 + 1  # last value used as "none"
    n_c = n_goals - 1
    dvars[w] = dict(type='saturating', dom=(0, n_w), owner='sys')
    dvars[c] = dict(type='saturating', dom=(0, n_c), owner='sys')
    # compile
    t = symbolic.Automaton()
    t.vars = dvars
    bdd = aut.bdd
    t.bdd = bdd
    t = t.build()
    env_init = aut.init['env'][0]
    sys_init = aut.init['sys'][0]
    env_action = aut.action['env'][0]
    sys_action = aut.action['sys'][0]
    goals = aut.win['[]<>']
    t.action['env'] = [env_action]
    # compute strategy from iterates
    # \rho_1: descent in persistence basin
    s = "({c}' = {c}) & ({w}' = {none})".format(
        c=c, w=w, none=n_holds)
    count = t.add_expr(s)
    rho_1 = bdd.false
    basin = zk[0]
    for z in zk[1:]:
        trans = _moore_trans(basin, t)
        rim = bdd.apply('diff', z, basin)
        u = bdd.apply('and', rim, trans)
        u = bdd.apply('and', u, count)
        rho_1 = bdd.apply('or', rho_1, u)
        basin = z
    rho_2 = bdd.false
    rho_3 = bdd.false
    rho_4 = bdd.false
    basin = bdd.false
    for z, yi, xijr in zip(zk, yki, xkijr):
        cox_basin = fx.ue_preimage(env_action, sys_action,
                                   basin, t)
        rim = bdd.apply('diff', z, basin)
        rim = bdd.apply('and', rim, -cox_basin)
        # rho_2: pick persistence set
        s = "({c}' = {c}) & ({w} = {none})".format(
            c=c, w=w, none=n_holds)
        count = t.add_expr(s)
        u = bdd.apply('and', rim, count)
        v = bdd.false
        for i, y in enumerate(yi):
            s = "{w}' = {i}".format(w=w, i=i)
            count = t.add_expr(s)
            trans = _moore_trans(y, t)
            q = bdd.apply('and', count, trans)
            v = bdd.apply('or', v, q)
        u = bdd.apply('and', u, v)
        rho_2 = bdd.apply('or', rho_2, u)
        # rho_3: descent in recurrence basin
        s = (
            "({c}' = {c}) &"
            "({w} != {none}) &"
            "({w}' = {w})").format(
                c=c, w=w, none=n_holds)
        count = t.add_expr(s)
        u = bdd.apply('and', rim, count)
        v = bdd.false
        for i, xjr in enumerate(xijr):
            for j, (xr, goal) in enumerate(zip(xjr, goals)):
                s = (
                    "({c} = {j}) &"
                    " ({w} = {i})").format(c=c, w=w, i=i, j=j)
                count = t.add_expr(s)
                x_basin = xr[0]
                p = bdd.false
                for x in xr[1:]:
                    trans = _moore_trans(x_basin, t)
                    q = bdd.apply('and', trans, -x_basin)
                    q = bdd.apply('and', x, q)
                    p = bdd.apply('or', p, q)
                    x_basin = x
                p = bdd.apply('and', p, count)
                p = bdd.apply('and', p, -goal)
                v = bdd.apply('or', v, p)
        u = bdd.apply('and', u, v)
        rho_3 = bdd.apply('or', rho_3, u)
        # rho_4: advance to next recurrence goal
        u = bdd.false
        for j, goal in enumerate(goals):
            jp = (j + 1) % len(goals)
            s = "({c} = {j}) & ({c}' = {jp})".format(
                c=c, j=j, jp=jp)
            count = t.add_expr(s)
            p = bdd.apply('and', count, goal)
            u = bdd.apply('or', u, p)
        s = (
            "({w} != {none}) &"
            "({w}' = {w})").format(
                c=c, w=w, none=n_holds)
        count = t.add_expr(s)
        u = bdd.apply('and', u, count)
        u = bdd.apply('and', u, rim)
        v = bdd.false
        for i, y in enumerate(yi):
            s = "{w} = {i}".format(w=w, i=i)
            count = t.add_expr(s)
            trans = _moore_trans(y, t)
            q = bdd.apply('and', count, trans)
            v = bdd.apply('or', v, q)
        u = bdd.apply('and', u, v)
        rho_4 = bdd.apply('or', rho_4, u)
        # update
        basin = z
    # \rho
    u = bdd.apply('or', rho_1, rho_2)
    u = bdd.apply('or', rho_3, u)
    u = bdd.apply('or', rho_4, u)
    u = bdd.apply('and', sys_action, u)
    # counter limits
    u = bdd.apply('and', t.action['sys'][0], u)
    if not aut.plus_one:
        u = bdd.apply('->', env_action, u)
    if aut.moore:
        u = bdd.forall(t.upvars, u)
    t.action['sys'] = [u]
    # initial condition for counter
    s = '({c} = 0) & ({w} = {none})'.format(
        c=c, w=w, none=n_holds)
    count = t.add_expr(s)
    # \A init
    init = _all_init(env_init, sys_init, count, bdd)
    t.init['env'] = [init]
    init = bdd.apply('->', init, win_set)
    assert init == bdd.true, 'losing from some init states'
    return t


def _all_init(env_init, sys_init, internal, bdd):
    """Initial condition conjoining for all variables."""
    # case of `ONE_SIDE_INIT` with `ENVINIT` in `gr1c`
    u = bdd.apply('and', sys_init, internal)
    u = bdd.apply('and', env_init, u)
    return u


def _moore_trans(target, aut):
    """Return controllable transitions for progress."""
    bdd = aut.bdd
    env_action = aut.action['env'][0]
    sys_action = aut.action['sys'][0]
    uvars = aut.upvars
    u = bdd.rename(target, aut.prime)
    if aut.plus_one:
        u = bdd.apply('->', env_action, u)
        u = bdd.apply('and', sys_action, u)
    else:
        u = bdd.apply('and', sys_action, u)
        u = bdd.apply('->', env_action, u)
    if aut.moore:
        u = bdd.forall(uvars, u)
    return u


def trivial_winning_set(aut_streett):
    """Return set of trivially winning nodes for Streett(1).

    @return: `(trivial, aut_streett)` where:
        - `trivial`: node in `aut_streett.bdd`
        - `aut_streett`: `symbolic.Automaton`
    """
    aut_rabin = symbolic.Automaton()
    for var, d in aut_streett.vars.iteritems():
        d = d.copy()
        owner = d['owner']
        owner = 'env' if owner == 'sys' else 'sys'
        d['owner'] = owner
        aut_rabin.vars[var] = d
    aut_rabin.action['env'] = aut_streett.action['sys']
    aut_rabin.action['sys'] = aut_streett.action['env']
    win = ['!({w})'.format(w=w) for w in aut_streett.win['<>[]']]
    aut_rabin.win['[]<>'] = win
    symbolic.fill_blanks(aut_rabin, rabin=True)
    aut_rabin.bdd = aut_streett.bdd
    aut_streett = aut_streett.build()
    aut_rabin = aut_rabin.build()
    # solve
    win_streett, _, _ = solve_streett_game(aut_streett)
    zk, _, _ = solve_rabin_game(aut_rabin)
    win_rabin = zk[-1]
    # find trivial win set
    # win_rabin_ = _copy_bdd(win_rabin,
    #                        aut_rabin.bdd, aut_streett.bdd)
    trivial = aut_streett.bdd.apply('diff', win_streett, win_rabin)
    return trivial, aut_streett


def _map_nested_lists(f, x, *arg, **kw):
    """Recursively map lists, with non-lists at the bottom.

    Useful for applying `dd.bdd.copy_bdd` to several lists.
    """
    if isinstance(x, list):
        return [_map_nested_lists(f, y, *arg, **kw) for y in x]
    else:
        return f(x, *arg, **kw)


def _copy_bdd(u, a, b):
    """Copy bdd `u` from manager `a` to `b`.

    No effect if `a is b`.
    """
    if a is b:
        return u
    return a.copy(u, b)
