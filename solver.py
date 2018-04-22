from SATInstance import SATInstance
from watchlist import update_watchlist, unit_pg
from utils import *
from sys import stderr
import copy

def recursive_solve(instance, watchlist, assignment, d, unit_propagation=False, verbose=False):
    """
    Recursively solve SAT by assigning to variables d, d+1, ..., n-1. Assumes
    variables 0, ..., d-1 are assigned so far. A generator for all the
    satisfying assignments is returned.
    """
    if d == len(instance.variables):
        yield assignment
        return


    # if unit_propagation:
    #     if unit_pg(instance, 
    #                 watchlist, 
    #                 assignment, 
    #                 unit_propagation, 
    #                 verbose):

    if unit_propagation:
        pp_assignment = copy.deepcopy(assignment)
        unit_pg(instance, watchlist, pp_assignment, unit_propagation, verbose)
        # print(pp_assignment, assignment)
        next_d = None
        for i in range(len(pp_assignment)):
            if pp_assignment[i] != assignment[i]:
                next_d = i
                # print(pp_assignment, assignment)
        if next_d != None:
            d = next_d

    # if not assignment[d] is None:
    #     return
    for a in [0, 1]:
        if verbose:
            print('Trying {} = {}'.format(instance.variables[d], a),
                  file=stderr)
        assignment[d] = a
        if update_watchlist(instance,
                            watchlist,
                            variable_to_literal(d, a),
                            assignment,
                            unit_propagation, 
                            verbose):
            for a in recursive_solve(instance, watchlist, assignment, d+1, unit_propagation, verbose):
                yield a

    assignment[d] = None