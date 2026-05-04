# Dijkstra

A CS-361 group project by Andrew Crowe and Nathan Stallman.  
</br>
We implement several versions of Dijkstra's shortest path algorithm where the only differences are the data structures they use for selecting next minimum-distance vertices. We then benchmark each version of the algorithm and analyze the impact of the different data structures on its runtime and memory efficiency across various input sizes.

## Usage

Execute the program from the command line by passing the desired operating mode:

`python3 main.py [MODE]`

**Available Modes:**

* `test` (alias: `pqt`): Run Priority Queue insertion and extraction tests.
* `minheap` (alias: `pq`): Execute Dijkstra's algorithm using a Min-Heap Priority Queue (Adjacency List).
* `arrlist` (alias: `al`): Execute Dijkstra's using an Array-based Priority Queue (Adjacency List).
* `arrmat` (alias: `am`): Execute Dijkstra's using an Array-based Priority Queue (Adjacency Matrix).
* `bench` (alias: `b`): Run GraphBenchmarker performance experiments.

## Progress Tracker  
### 4.1
* Introduction/background draft complete - *Andrew* 
### 4.2 - 4.3
* Adjacency list and matrix implemented - *Nathan*
* Dynamic dense graph generator implemented - *Nathan*
* Min-heap priority queue implemented - *Andrew*
* PQ Dijkstra implemented - *Andrew*
* Array Dijkstras implemented - *Nathan*
### 4.4 - 4.5
* Benchmarking suite implemented  - *Andrew*
* Record and analyze benchmark data - *Nathan*

## TODO
* Section 7
* Section 8
