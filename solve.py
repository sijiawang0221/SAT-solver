from SATInstance import SATInstance
from solver import recursive_solve
from watchlist import setup_watchlist
from testcase_generator import testcase_generator
import numpy as np
import time

len_CNF = 100      # length of CNF
# num_var = 26        # number of variables
num_testcase = 20   # number of test cases

def main():
    mean = [[0, 0] for i in range(90)]
    for num_var in range(10,100):
        testcase_generator(len_CNF,num_var,num_testcase)
        res = np.zeros((num_testcase, 2))
        for test_id in range(num_testcase):
            # print(test_id)
            test_file = 'test/testcase'+str(test_id)+'.txt'
            # test_file = 'test/test.txt'

            with open(test_file) as file:
                instance = SATInstance.from_file(file)
            watch_list = setup_watchlist(instance)
            n = len(instance.variables)
            upp = True
            assignments1 = [None] * n
            start_time1 = time.time()
            assignment1 = recursive_solve(instance, watch_list, assignments1, 0, not upp)
            # for assignment in assignments:
            #     print(instance.assignment_to_string(assignment))
            end_time1 = time.time()
            # print(end_time1 - start_time1)
            res[test_id][0] = end_time1 - start_time1

            with open(test_file) as file:
                instance2 = SATInstance.from_file(file)
            watch_list2 = setup_watchlist(instance2)
            n = len(instance2.variables)

            assignments2 = [None] * n
            start_time2 = time.time()
            assignment2 = recursive_solve(instance2, watch_list2, assignments2, 0, upp)
            # for assignment in assignments:
            #     print(instance.assignment_to_string(assignment))

            end_time2 = time.time()
            # print(end_time2 - start_time2)
            res[test_id][1] = end_time2 - start_time2

        temp1 = np.mean(res[:][0])
        temp2 = np.mean(res[:][1])
        mean[num_var-10][0] = temp1
        mean[num_var-10][1] = temp2
        # print(res)
    np.set_printoptions(precision=3)
    print(mean)
    return

if __name__ == '__main__':
    main()
