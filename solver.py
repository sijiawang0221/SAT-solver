from SATInstance import SATInstance
from watchlist import update_watchlist
from utils import *
from sys import stderr

def recursive_solve(instance, watchlist, assignment, d, verbose):
    """
    Recursively solve SAT by assigning to variables d, d+1, ..., n-1. Assumes
    variables 0, ..., d-1 are assigned so far. A generator for all the
    satisfying assignments is returned.
    """
    if d == len(instance.variables):
        yield assignment
        return

    for a in [0, 1]:
        if verbose:
            print('Trying {} = {}'.format(instance.variables[d], a),
                  file=stderr)
        assignment[d] = a
        if update_watchlist(instance,
                            watchlist,
                            variable_to_literal(d, a),
                            assignment,
                            verbose):
            for a in recursive_solve(instance, watchlist, assignment, d + 1, verbose):
                yield a

    assignment[d] = None