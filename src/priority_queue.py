class DijkstraMinHeap:
    def __init__(self, max_vertices, debug=False):
        self.capacity = max_vertices
        self.size = 0                   # Elements in the heap
        self.harr = []                  # Stores [distance, vertex]
        self.pos = [-1] * max_vertices  # Maps vertex ID to its index in harr
        self.debug = debug

    # Helper methods
    def parent(self, i): return (i - 1) // 2 # parent node index
    def left(self, i): return 2 * i + 1      # left child index
    def right(self, i): return 2 * i + 2     # right child index

    def is_empty(self):
        return self.size == 0

    def swap(self, i, j):
        nodeI, nodeJ = self.harr[i][1], self.harr[j][1]
        self.pos[nodeI] = j
        self.pos[nodeJ] = i
        self.harr[i], self.harr[j] = self.harr[j], self.harr[i]

    def minHeapify(self, i):
        l, r = self.left(i), self.right(i)
        smallest = i
        if l < self.size and self.harr[l][0] < self.harr[smallest][0]:
            smallest = l
        if r < self.size and self.harr[r][0] < self.harr[smallest][0]:
            smallest = r
        if smallest != i:
            self.swap(i, smallest)
            self.minHeapify(smallest)

    def extractMin(self):
        if self.is_empty(): return None
        root = self.harr[0]        # min dist root node
        last_node = self.harr[self.size - 1]
        self.harr[0] = last_node
        self.pos[last_node[1]] = 0 # update pos map
        self.pos[root[1]] = -1     # mark extracted as removed
        self.size -= 1
        self.harr.pop()            # remove last
        # Restore min heap
        if self.size > 0:
            self.minHeapify(0)
        return root

    def decreaseKey(self, vertex, new_dist):
        i = self.pos[vertex]
        if i == -1: return
        self.harr[i][0] = new_dist
        while i != 0 and self.harr[self.parent(i)][0] > self.harr[i][0]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def insertKey(self, vertex, dist):
        if self.size == self.capacity: return # heap is full
        self.harr.append([dist, vertex])
        i = self.size
        self.pos[vertex] = i
        self.size += 1
        # Bubble up to resotre heap property
        while i != 0 and self.harr[self.parent(i)][0] > self.harr[i][0]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def isInMinHeap(self, vertex):
        return self.pos[vertex] != -1 if vertex < len(self.pos) else False