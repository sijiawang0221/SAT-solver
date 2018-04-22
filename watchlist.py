from SATInstance import SATInstance
from utils import *
import copy

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
                     unit_propagation, 
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

def propagatable(assignment, clause):
    clause = list(clause)
    not_assigned_literal = None
    for literal in clause:
        variable_assignment = assignment[literal_to_variable(literal)]
        if variable_assignment == None:
            if not_assigned_literal == None:
                    not_assigned_literal = literal    
            else:
                return False, None
        elif variable_assignment == negate(is_negated(literal)):
                return False, None
        # if is_negated(literal):
        #     if not assignment[literal_to_variable(literal)] == 0:
        #         return False, None
        # else:
        #     if not assignment[literal_to_variable(literal)] == 1:
        #         return False, None
        
    if not_assigned_literal == None:
        return False, None
    return True, not_assigned_literal
        

def unit_pg_step(instance,
            watchlist,
            assignment,
            unit_propagation, 
            verbose):
    false_literal = None
    for clause in instance.clauses:
        is_propagatable, literal = propagatable(assignment, clause)
        if is_propagatable:
            assignment[literal_to_variable(literal)] = negate(is_negated(literal))
            # if is_negated(literal):
            #     assignment[literal_to_variable(literal)] = 0
            # else:
            #     assignment[literal_to_variable(literal)] = 1
            false_literal = negate(literal)
            break
    if false_literal is None:
        return
    print("Unit propagation: ", false_literal)
    return update_watchlist(instance, 
                            watchlist, 
                            false_literal, 
                            assignment, 
                            unit_propagation, 
                            verbose)
def unit_pg(instance,
            watchlist,
            assignment,
            unit_propagation, 
            verbose):
    
    last_assignment = copy.deepcopy(assignment)
    unit_pg_step(instance, watchlist, assignment, unit_propagation, verbose)
    while not last_assignment == assignment:
        last_assignment = copy.deepcopy(assignment)
        unit_pg_step(instance, watchlist, assignment, unit_propagation, verbose)


