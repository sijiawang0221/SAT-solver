# SAT-solver with Unit Propagation

We implemented a simple SAT solver to solve SAT problems efficiently. Our algorithm is a watch-list based backtracking algorithm. There is very little, practically nothing, needs to be done to "undo" steps when we were using backtracking. Moreover, the unit propagation also benefit from the watch-list data structure. The cost of propagating one single literal is quite marginal. 
