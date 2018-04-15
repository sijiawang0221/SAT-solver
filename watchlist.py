from SATInstance import SATInstance
from utils import *

def setup_watchlist(instance):
    watchlist = [list() for __ in range(2 * len(instance.variables))]
    for clause in instance.clauses:
        # Make the clause watch its first literal
        watchlist[clause[0]].append(clause)
    return watchlist

def update_watchlist(instance,
                     watchlist,
                     false_literal,
                     assignment,
                     verbose):
    """
    Updates the watch list after literal 'false_literal' was just assigned
    False, by making any clause watching false_literal watch something else.
    Returns False it is impossible to do so, meaning a clause is contradicted
    by the current assignment.
    """
    while watchlist[false_literal]:
        clause = watchlist[false_literal][0]
        found_alternative = False
        for alternative_literal in clause:
            v = literal_to_variable(alternative_literal)
            a = is_negated(alternative_literal)
            if assignment[v] is None or not assignment[v] == a:
                found_alternative = True
                del watchlist[false_literal][0]
                watchlist[alternative_literal].append(clause)
                break

        if not found_alternative:
            # if verbose:
            #     dump_watchlist(instance, watchlist)
            #     print('Current assignment: {}'.format(
            #           instance.assignment_to_string(assignment)),
            #           file=stderr)
            #     print('Clause {} contradicted.'.format(
            #           instance.clause_to_string(clause)),
            #           file=stderr)
            return False
    return True