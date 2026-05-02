# Dijkstra

A CS-361 group project by Andrew Crowe and Nathan Stallman.  
</br>
We implement several versions of Dijkstra's shortest path algorithm where the only differences are the data structures they use for selecting next minimum-distance vertices. We then benchmark each version of the algorithm and analyze the impact of the different data structures on its runtime and memory efficiency.

## Usage

Execute the program from the command line by passing the desired operating mode:

`python3 main.py [mode]`

**Available Modes:**

* `test_pq`: Runs the priority queue validation tests.
* `pq_dijkstra`: Executes the Min-Heap/Priority Queue version of Dijkstra's algorithm.
* `arr_dijkstra_list`: Executes the Array based version of Dijkstra's algorithm over an adjacecncy list (WIP).
* `arr_dijkstra_mat`: Executes the Array based version of Dijkstra's algorithm over an adjacecncy matrix (WIP).
* `array_matrix`: Runs the Array-Based (Adjacency Matrix) version (WIP).
* `array_list`: Runs the Array-Based (Adjacency List) version (WIP).
* `benchmark`: Runs performance and memory measurements across all implementations (WIP).

## Progress Tracker  
### 4.1
* Introduction/background draft complete - *Andrew*  
### 4.2-4.3
* Adjacency list and matrix implemented - *Nathan*
* Random dense graph generator implemented - *Nathan*
* Min-heap priority queue implemented - *Andrew*
* PQ Dijkstra implemented - *Andrew*

## TODO

* **4.2 - 4.3** Fix adj matrix, make sure adj list works as intended
* **4.4** Benchmark algorithms according to Section 6
* **4.5** Write analysis according to Section 7
