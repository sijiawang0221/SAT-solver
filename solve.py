from SATInstance import SATInstance
from solver import recursive_solve
from watchlist import setup_watchlist
import time

test_file = 'test/test.txt'
# test_file = 'test/w44-008.txt'
with open(test_file) as file:
    instance = SATInstance.from_file(file)
watch_list = setup_watchlist(instance)
n = len(instance.variables)

upp_first = False
assignments = [None] * n
start_time = time.time()
assignments = recursive_solve(instance, watch_list, assignments, 0, upp_first)
end_time = time.time()
for assignment in assignments:
    print(instance.assignment_to_string(assignment))
print(end_time - start_time)

assignments = [None] * n
start_time = time.time()
assignments = recursive_solve(instance, watch_list, assignments, 0, not upp_first)
end_time = time.time()
for assignment in assignments:
    print(instance.assignment_to_string(assignment))
print(end_time - start_time)