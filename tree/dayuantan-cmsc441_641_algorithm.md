# DayuanTan/CMSC441\_641\_algorithm

## CMSC441 & 641 Algorithm

This is a private place where I record my reviewing, thinking and reorganizaiton for "Algorithm" course.

## 1. Sorting

| Time | [![](https://camo.githubusercontent.com/4293e25fe5d8c1b7c4e2c94622b205746875fef6/68747470733a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f245c5468657461286e5e322924)](https://www.codecogs.com/eqnedit.php?latex=$$\Theta%28n^2%29$$) | [![](https://camo.githubusercontent.com/d79d3fdd89527b680ba1380b9f2a5e138c46a20f/68747470733a2f2f6c617465782e636f6465636f67732e636f6d2f6769662e6c617465783f245c5468657461286e6c6f676e2924)](https://www.codecogs.com/eqnedit.php?latex=$$\Theta%28n^2%29$$) |
| :--- | :--- | :--- |
| Sorting Algorithms | [Insert Sort \(sort in place\)](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/insertsort) | [Merge Sort](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/mergesort) |
| [Heap Sort \(sort in place\)](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/heapsort) |  |  |
| [Quick Sort \(Worst\)](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/quicksort) | [Quick Sort \(Avg\) \(sort in place\)](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/quicksort) |  |

## 2. Dynamic Programming

“Programming” in this context refers to a tabular method, not to writing computer code.

### 2.1 Divide-and-conquer VS Dynamic progrmming alg

[![](../.gitbook/assets/venn_dpalg%20%281%29.png)](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/DynamicProg/venn_DPalg.png)

 [GO TO TOP.](dayuantan-cmsc441_641_algorithm.md#cmsc441_algorithm)

### 2.2 Four steps for Dynamic Programming alg:

1. Characterize the structure of an optimal solution.
2. Recursively deﬁne the value of an optimal solution.
3. Compute the value of an optimal solution, typically in a bottom-up fashion.
4. Construct an optimal solution from computed information.

### 2.3 Characteristics

_**optimal substructure**_: optimal solutions to a problem incorporate/consists of optimal solutions to related subproblems, which we may solve independently.

 [GO TO TOP.](dayuantan-cmsc441_641_algorithm.md#cmsc441_algorithm)

### 2.4 Two ways to implement a dynamic-programming approach

#### 2.4.1 top-down with memoization

* Recursively sovle problems as usual and memoized.
* But in each recursion frst check whether this subproblem has previously solved.

#### 2.4.2 down-top

* Sort subproblems in size and solve them in size order.
* When solving a particular subproblem, we have already solved all of the smaller subproblems its solution depends upon, and we have saved their solutions

Dynamic programming thus **uses additional memory to save computation time**; it serves an example of a **time-memory trade-off**. The savings may be dramatic: an exponential-time solution may be transformed into a polynomial-time solution. A dynamic-programming approach runs in polynomial time when the number of distinct subproblems involved is polynomial in the input size and we can solve each such subproblem in polynomial time.

 [GO TO TOP.](dayuantan-cmsc441_641_algorithm.md#cmsc441_algorithm)

### 2.5 Examples

#### [2.5.1 Rod Cutting](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/DP_rodcutting/rodcutting.md)

#### [2.5.2 Car Ownership](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/DP_carowner/carowner.md)

#### [2.5.3 Stamp Collection](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/DP_stampCollection/stampColletion.md)

#### [2.5.4 Waldo's World](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/DP_waldoworld/waldoWorld.md)

 [GO TO TOP.](dayuantan-cmsc441_641_algorithm.md#cmsc441_algorithm)

## 3. Greedy Alg

### 3.1 Theory

### 3.2 Examples

#### [3.2.1 Greedy Activity Selection](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/Greedy_gas/Eg_GreedyActivitySelection.md)

#### [3.2.2 Greedy Trick or Treat](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/Greedy_tricktreat/eg_greedytricktreat.md)

#### [3.2.3 Professor Gekko's skating expedition](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/Greedy_skating/eg_greedyskating.md)

#### [3.2.4 Unit-length intervals](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/Greedy_unitLengthInterval/eg_unitLengthInterval.md)

 [GO TO TOP.](dayuantan-cmsc441_641_algorithm.md#cmsc441_algorithm)

## 4. Graph Theory

### 4.1 Graph

**Graph**: G = \(V, E\). Self loop: \(v, v\).

**Undirected Graph**: Wire, Traffic netowkrs.

**Directed Graph**: Status transition, Markov model.

**Sparse Graph**: \|E\| &lt;&lt; $\|V\|^2$.

**Dense Graph**: \|E\| $\approx$&lt; $\|V\|^2$.

**Weighted Graph**: Distance, Density.

**Adjacency-list** representation V.S. **Adjacency-matrix** representation:

[![](../.gitbook/assets/graph_representation%20%281%29.png)](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/Graph/graph_representation.png)

When programming, how represent adjacency-list?

* List, forward list.
* Vector. // Don't change often. Quicker. Easy for reading and writing.
* Set, unordered set. // Easy for looking up.

[![](../.gitbook/assets/graph_vector%20%281%29.png)](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/Graph/graph_vector.png)

**Searching Algorithms:**

* **BFS**: Like water wave. Similiar to Tree‘s hierarchy traversal but the difference is we need to label whether we have visited this node or not, which is not necessary in THT.
  * Code: [cpp](https://github.com/xiexiexx/Planet/blob/master/breadth_first_search/BFS.cpp)\([Backup](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/Graph/BFS.cpp)\).
* **DFS**: Widely used. Try best to visit as deeply as possible.
  * Code:.

For more, see [slides of Dr. Chang](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/Graph/12.1%20Graph%20Algorithms.pdf).

### 4.2 Example

#### [4.2.1 Two Coloring](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/Graph_2coloring/eg_2coloring.md)

#### [4.2.2 Reachability](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/Graph_reachability/eg_reachability.md)

### 4.3

### 4.4 Example

#### [4.4.1 Alternate topology sort](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/Graph_alternateTopologySort/eg_alternateTopologySort.md)

#### [4.4.2 Semiconnected](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/Graph_semiconnected/eg_semiconnected.md)

#### [4.4.3 Gossip Mongering](https://github.com/DayuanTan/CMSC441_641_algorithm/blob/5f6d2ecd9f6932c86157a96b3574222e78998a69/Graph_gossipMongering/eg_gossipMongering.md)

 [GO TO TOP.](dayuantan-cmsc441_641_algorithm.md#cmsc441_algorithm)

