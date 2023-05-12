from z3 import *

def missing_number(l: list) -> int:
    """Returns the number that is not in the list."""
    m = Int('m')
    s = Solver()
    equations = [m != IntVal(element) for element in l]
    equations.append(m >= 1)
    equations.append(m <= IntVal(len(l) + 1))
    s.add(equations)
    return s.model().evaluate(m).as_long() if (s.check() == sat) else None
