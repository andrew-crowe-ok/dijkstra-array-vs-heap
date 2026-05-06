# Dijkstra: Array vs. Heap
### A group project by Andrew Crowe and Nathan Stallman.  
</br>
We implement several versions of Dijkstra's single source shortest path algorithm where the only differences are the data structures they use for selecting next minimum-distance vertices. We then benchmark each implementation of the algorithm and analyze the impact of the different data structures on its runtime and memory efficiency across various input sizes.  

## Usage

Execute the program from the command line by passing the desired operating mode:

`python3 main.py [MODE]`

**Available Modes:**

* `test` (alias: `pqt`): Run priority queue insertion and extraction tests.
* `minheap` (alias: `pq`): Execute Dijkstra's using a Min-Heap priority queue.
* `arrlist` (alias: `al`): Execute Dijkstra's using an array-based priority queue (Adjacency List).
* `arrmat` (alias: `am`): Execute Dijkstra's using an array-based priority queue (Adjacency Matrix).
* `bench` (alias: `b`): Run GraphBenchmarker performance experiments.
</br>
Running benchmarks will create benchmark_results.csv. An R script, plot_benchmarks.R, was used to plot the data in R Studio. 
