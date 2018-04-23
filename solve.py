from SATInstance import SATInstance
from solver import recursive_solve
from watchlist import setup_watchlist
from testcase_generator import testcase_generator
import time

len_CNF = 30      # length of CNF
num_var = 5       # number of variables
num_testcase = 5  # number of test cases

def main():
    testcase_generator(len_CNF,num_var,num_testcase)
    for test_id in range(num_testcase):
        test_file = 'test/testcase'+str(test_id)+'.txt'
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

if __name__ == '__main__':
    main()
