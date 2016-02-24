"""
Set up range of initial data for the reactive Riemann problem and see if the
wave pattern changes with tangential velocity.
"""
from r3d2 import eos_defns, State, RiemannProblem
from itertools import combinations

def check_wave_pattern(U_reactive, U_burnt, vts=[-0.9,0.0,0.9]):
    """
    Given an initial reactive state and burnt state, will run the
    reactive Riemann problem with the reactive state having a range
    of tangential velocities. Shall print output to screen where the
    resulting wave patterns are different.
    """
    wave_patterns = []
    for vt in vts:
    # first change the vt
        U_reactive.vt = vt
        rp = RiemannProblem(U_reactive, U_burnt)
        wave_patterns.append(rp.waves)

    # now check if all the wave patterns are the same

    # flatten patterns
    flat_patterns = []
    for i, p in enumerate(wave_patterns):
        flat_patterns.append([])
        for w in p:
            for s in w.wave_sections:
                flat_patterns[i].append(repr(s))

    # generate list of pairs
    pairs = list(combinations(range(len(vts)), 2))

    # check to see if patterns match
    for i, j in pairs:
        if not flat_patterns[i] == flat_patterns[j]:
            print('vt = {}, {} are different'.format(vts[i], vts[j]))
            print(' '.join(flat_patterns[i]))
            print(' '.join(flat_patterns[j]))


if __name__ == "__main__":
    eos = eos_defns.eos_gamma_law(5.0/3.0)
    eos_reactive = eos_defns.eos_gamma_law_react(5.0/3.0, 0.1, 1.0, 1.0, eos)
    U_reactive = State(5.0, 0.0, 0.0, 2.0, eos_reactive)
    U_burnt = State(8.113665227084942, -0.34940431910454606, 0.0,
                    2.7730993786742353, eos)

    check_wave_pattern(U_reactive, U_burnt)