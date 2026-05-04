# Dijkstra

A CS-361 group project by Andrew Crowe and Nathan Stallman.  
</br>
We implement several versions of Dijkstra's shortest path algorithm where the only differences are the data structures they use for selecting next minimum-distance vertices. We then benchmark each version of the algorithm and analyze the impact of the different data structures on its runtime and memory efficiency across various input sizes.

## Usage

Execute the program from the command line by passing the desired operating mode:

`python3 main.py [MODE]`

**Available Modes:**

* `test` (aliases: `pqt`, `pq_test`): Run Priority Queue insertion and extraction tests.
* `minheap` (aliases: `pq`, `pq_dijkstra`): Execute Dijkstra's algorithm using a Min-Heap Priority Queue (Adjacency List).
* `arrlist` (aliases: `al`, `arr_dijkstra_list`): Execute Dijkstra's using an Array-based Priority Queue (Adjacency List).
* `arrmat` (aliases: `am`, `arr_dijkstra_mat`): Execute Dijkstra's using an Array-based Priority Queue (Adjacency Matrix).
* `bench` (aliases: `b`, `benchmark`): Run GraphBenchmarker performance experiments.

## Progress Tracker  
### 4.1
* Introduction/background draft complete - *Andrew* 
### 4.2 - 4.3
* Adjacency list and matrix implemented - *Nathan*
* Dynamic dense graph generator implemented - *Nathan*
* Min-heap priority queue implemented - *Andrew*
* PQ Dijkstra implemented - *Andrew*
* Array Dijkstra implemented - *Nathan*
* Benchmarking suite implemented  - *Andrew*
### 4.4 - 4.5
* Record and analyze benchmark data - *Nathan*

## TODO
* Section 7
* Section 8