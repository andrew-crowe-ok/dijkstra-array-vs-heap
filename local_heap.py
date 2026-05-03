"""

# Directed graph
MY_NODES_ONE = {"1_Albuquerque", "2_Santa Fe", "3_Las Cruces", "4_Gallup", 
                "5_Taos", "6_Clayton", "7_Capulin", "8_Truth or Consequences",
                "9_Ruidoso", "10_Shiprock", "11_Farmington"}
MY_EDGES_ONE = [
    ("Albuquerque", "Santa Fe", 7), ("Albuquerque", "Las Cruces", 10), ("Santa Fe", "Gallup", 6), 
    ("Santa Fe", "Taos", 8), ("Las Cruces", "Clayton", 3), ("Las Cruces", "Capulin", 2),
    ("Gallup", "Truth or Consequences", 4), ("Gallup", "Ruidoso", 2), ("Taos", "Shiprock", 3), 
    ("Taos", "Farmington", 5), ("Clayton", "Ruidoso", 3), ("Capulin", "Albuquerque", 14), 
    ("Truth or Consequences", "Capulin", 13), ("Ruidoso", "Farmington", 1), ("Shiprock", "Farmington", 11)    
]

"""

import sys
import random

class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap_size = 0
        self.harr = []  # Stores tuples of (weight, key)

    def parent(self, i): return (i - 1) // 2
    def left(self, i): return 2 * i + 1
    def right(self, i): return 2 * i + 2

    def insertKey(self, key, weight, r):
        if self.heap_size == self.capacity:
            print("\nOverflow: Could not insertKey")
            return

        self.heap_size += 1
        self.harr.append((weight, key))
        i = self.heap_size - 1

        if r and self.heap_size <= 31:
            self.printTree()

        # Fix the min heap property if it is violated (comparing by weight)
        while i != 0 and self.harr[self.parent(i)][0] > self.harr[i][0]:
            self.harr[i], self.harr[self.parent(i)] = self.harr[self.parent(i)], self.harr[i]
            i = self.parent(i)

            if r and self.heap_size <= 31:
                self.printTree()

    def decreaseKey(self, i, new_weight):
        key = self.harr[i][1]
        self.harr[i] = (new_weight, key)
        while i != 0 and self.harr[self.parent(i)][0] > self.harr[i][0]:
            self.harr[i], self.harr[self.parent(i)] = self.harr[self.parent(i)], self.harr[i]
            i = self.parent(i)

    def extractMin(self):
        if self.heap_size <= 0:
            return float('inf')
        if self.heap_size == 1:
            self.heap_size -= 1
            return self.harr.pop()

        # Store the minimum key, and remove it from heap
        root = self.harr[0]
        self.harr[0] = self.harr[-1]
        self.harr.pop()
        self.heap_size -= 1
        self.MinHeapify(0)

        print(f"Removed   :: W:{root[0]} K:{root[1]}")
        if self.heap_size > 0:
            print(f"New root  :: W:{self.harr[0][0]} K:{self.harr[0][1]}")
        print(f"Heap size :: {self.heap_size}")

        return root

    def deleteKey(self, i):
        node = self.harr[i]
        self.decreaseKey(i, float('-inf'))

        # Extract manually to prevent extractMin() from printing
        if self.heap_size == 1:
            self.heap_size -= 1
            self.harr.pop()
        else:
            self.harr[0] = self.harr[-1]
            self.harr.pop()
            self.heap_size -= 1
            self.MinHeapify(0)

        print(f"Removed :: key {node[1]} (weight {node[0]}) at index {i}")

    def MinHeapify(self, i):
        if self.heap_size <= 31:
            self.printTree()

        l = self.left(i)
        r = self.right(i)
        smallest = i

        if l < self.heap_size and self.harr[l][0] < self.harr[i][0]:
            smallest = l
        if r < self.heap_size and self.harr[r][0] < self.harr[smallest][0]:
            smallest = r
        if smallest != i:
            self.harr[i], self.harr[smallest] = self.harr[smallest], self.harr[i]
            self.MinHeapify(smallest)

    def printHeap(self):
        if self.heap_size == 0:
            print("Heap is empty.")
            return

        for w, k in self.harr:
            if w == k:
                print(f"{k}", end=" ")
            else:
                print(f"({w}:{k})", end=" ")
        print()

    def printTree(self):
        if self.heap_size == 0:
            print("Heap is empty.")
            return

        print("\n--- Top-Down Heap Tree ---\n")

        # Calculate total depth of the heap
        depth = 0
        temp = self.heap_size
        while temp > 0:
            depth += 1
            temp //= 2

        index = 0
        for i in range(depth):
            level_nodes = 1 << i  # Number of nodes at current level
            space_between = (1 << (depth - i)) - 1  # Spaces between nodes
            leading_space = space_between // 2  # Initial offset for the row

            print("    " * leading_space, end="")

            for j in range(level_nodes):
                if index < self.heap_size:
                    w, k = self.harr[index]
                    # Print as Key if weight matches, else Weight:Key
                    node_str = f"{k}" if w == k else f"{w}:{k}"
                    print(f"{node_str:>4}", end="")
                    index += 1
                    print("    " * space_between, end="")
            print("\n\n", end="")
        print("--------------------------")


def insertRandom(h, n):
    if not h:
        print("Error: Heap not created. Use 'create <size>' first.")
        return

    for _ in range(n):
        key = random.randint(0, 99)
        weight = random.randint(0, 99)
        h.insertKey(key, weight, False)


def print_help():
    print("\n--- Available Commands ---")
    print("create <size>           : Initialize the min-heap with a specific capacity")
    print("random <size>           : Generate a min-heap with n random numbers and weights")
    print("insert <key> [weight]   : Insert a key into the min-heap (weight defaults to key)")
    print("delete <index>          : Delete an index from the min-heap")
    print("decrease <index> <weight>: Decrease the weight of a key at the given index")
    print("kx <K> <X>              : Determine whether the heap contains K elements with weight smaller than X")
    print("min                     : Display the minimum key")
    print("extract                 : Remove the minimum (root) key")
    print("print                   : Display the min-heap as an array")
    print("tree                    : Display the min-heap as a tree")
    print("help                    : Show this help menu")
    print("exit                    : Exit the program")
    print("--------------------------")


def explore(h, i, k, x):
    if k <= 0 or i >= h.heap_size or h.harr[i][0] >= x:
        return 0

    leftSubTree = explore(h, h.left(i), k - 1, x)
    rightSubTree = explore(h, h.right(i), k - 1 - leftSubTree, x)

    return 1 + leftSubTree + rightSubTree


def kSmallerThanX(h, k, x):
    return explore(h, 0, k, x) >= k
 

def main():
    h = None
    print_help()

    while True:
        try:
            input_line = input("heap> ")
        except EOFError:
            break

        args = input_line.strip().split()
        if not args:
            continue

        cmd = args[0]
        argc = len(args)

        if cmd == "exit":
            break
        elif cmd == "print":
            if not h: print("Error: Heap not created. Use 'create <size>' first.")
            else: h.printHeap()
        elif cmd == "create" and argc == 2:
            if h:
                print("Old heap destroyed, new empty heap created")
            h = MinHeap(int(args[1]))
        elif cmd == "insert" and argc >= 2:
            if not h:
                print("Error: Heap not created. Use 'create <size>' first.")
            else:
                key = int(args[1])
                weight = int(args[2]) if argc >= 3 else key
                h.insertKey(key, weight, True)
        elif cmd == "delete" and argc == 2:
            if not h:
                print("Error: Heap not created. Use 'create <size>' first.")
            else:
                index = int(args[1])
                if index < 0 or index >= h.heap_size:
                    print("Error: Index out of bounds.")
                else:
                    h.deleteKey(index)
        elif cmd == "decrease" and argc == 3:
            if not h:
                print("Error: Heap not created. Use 'create <size>' first.")
            else:
                index = int(args[1])
                new_weight = int(args[2])
                if index < 0 or index >= h.heap_size:
                    print("Error: Index out of bounds.")
                elif new_weight > h.harr[index][0]:
                    print("Error: New weight is greater than current weight.")
                else:
                    h.decreaseKey(index, new_weight)
                    print(f"Decreased weight at index {index} to {new_weight}.")
        elif cmd == "extract":
            if not h:
                print("Error: Heap not created. Use 'create <size>' first.")
            else:
                h.extractMin()
        elif cmd == "min":
            if not h:
                print("Error: Heap not created. Use 'create <size>' first.")
            elif h.heap_size > 0:
                w, k = h.harr[0]
                if w == k:
                    print(f"{k}")
                else:
                    print(f"W:{w} K:{k}")
            else:
                print("Error: Heap is empty.")
        elif cmd == "help":
            print_help()
        elif cmd == "random" and argc == 2:
            n = int(args[1])
            if h:
                print("Old heap destroyed, new empty heap created")
            h = MinHeap(n)
            print(f"Created new heap with capacity {n}")
            insertRandom(h, n)
        elif cmd == "kx" and argc == 3:
            k = int(args[1])
            x = int(args[2])
            if not h:
                print("Error: Heap not created. Use 'create <size>' first.")
            else:
                result = kSmallerThanX(h, k, x)
                print(f"Does this min-heap contain {k} elements with weight smaller than {x}?\n {'True' if result else 'False'}.")
        elif cmd == "tree":
            if not h:
                print("Error: Heap not created. Use 'create <size>' first.")
            elif h.heap_size > 31:
                print(f"Error: Heap size ({h.heap_size}) exceeds the maximum printable tree size of 31.")
            else:
                h.printTree()
        else:
            print("Invalid command. Type 'help' for a list of available commands.")


if __name__ == "__main__":
    main()