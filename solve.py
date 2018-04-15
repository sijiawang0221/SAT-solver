from SATInstance import SATInstance
from solver import recursive_solve
from watchlist import setup_watchlist

test_file = 'test.txt'
with open(test_file) as file:
    instance = SATInstance.from_file(file)
watch_list = setup_watchlist(instance)
n = len(instance.variables)
assignments = [None] * n

assignments = recursive_solve(instance, watch_list, assignments, 0, False)

for assignment in assignments:
    print(instance.assignment_to_string(assignment))