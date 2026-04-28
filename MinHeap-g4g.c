/*
 * A MinHeap implementation in C, mostly taken from GeeksforGeeks.
 *
 * Written for CS-361 Homework 3, Problem 1: "Design an algorithm
 * that determines if there are k values less than x in the heap.
 * The solution must run in O(k) time."
 */

#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>

// Prototype of a utility function to swap two integers
void swap(int *x, int *y);

// A structure to represent a Min Heap
struct MinHeap
{
    int *harr;
    int capacity;
    int heap_size;
};

// Function prototypes
struct MinHeap *createMinHeap(int capacity);
void MinHeapify(struct MinHeap *h, int i);
void printHeap(struct MinHeap *h);
void printTree(struct MinHeap *h);
int parent(int i)
{
    return (i - 1) / 2;
}
int left(int i)
{
    return (2 * i + 1);
}
int right(int i)
{
    return (2 * i + 2);
}

int extractMin(struct MinHeap *h);
void decreaseKey(struct MinHeap *h, int i, int new_val);
int getMin(struct MinHeap *h)
{
    return h->harr[0];
}

void deleteKey(struct MinHeap *h, int i);
void insertKey(struct MinHeap *h, int k, bool r);

// Constructor: Creates a heap of given capacity
struct MinHeap *createMinHeap(int capacity)
{
  struct MinHeap *h = (struct MinHeap *)malloc(sizeof(struct MinHeap));
  h->heap_size = 0;
  h->capacity = capacity;
  h->harr = (int *)malloc(capacity * sizeof(int));
  return h;
}

// Inserts a new key 'k'
void insertKey(struct MinHeap *h, int k, bool r)
{
  if (h->heap_size == h->capacity)
  {
    printf("\nOverflow: Could not insertKey\n");
    return;
  }

  // First insert the new key at the end
  h->heap_size++;
  int i = h->heap_size - 1;
  h->harr[i] = k;

  if (r && h->heap_size <= 31) printTree(h);

  // Fix the min heap property if it is violated
  while (i != 0 && h->harr[parent(i)] > h->harr[i])
  {
    swap(&h->harr[i], &h->harr[parent(i)]);
    i = parent(i);

    if (r && h->heap_size <= 31) printTree(h);
  }
}

// Decreases value of key at index 'i' to new_val.
void decreaseKey(struct MinHeap *h, int i, int new_val)
{
    h->harr[i] = new_val;
    while (i != 0 && h->harr[parent(i)] > h->harr[i])
    {
        swap(&h->harr[i], &h->harr[parent(i)]);
        i = parent(i);
    }
}

// Function to remove minimum element (or root) from min heap
int extractMin(struct MinHeap *h)
{
  if (h->heap_size <= 0) return INT_MAX;
  if (h->heap_size == 1)
  {
    h->heap_size--;
    return h->harr[0];
  }

  // Store the minimum value, and remove it from heap
  int root = h->harr[0];
  h->harr[0] = h->harr[h->heap_size - 1];
  h->heap_size--;
  MinHeapify(h, 0);

  printf("Removed   :: %d\n", root);
  printf("New root  :: %d\n", h->harr[0]);
  printf("Heap size :: %d\n", h->heap_size);

  return root;
}

// This function deletes key at index i.
void deleteKey(struct MinHeap *h, int i)
{
  int val = h->harr[i];

  decreaseKey(h, i, INT_MIN);

  // Extract the INT_MIN root manually to prevent extractMin() from printing
  if (h->heap_size == 1)
  {
    h->heap_size--;
  }
  else
  {
    h->harr[0] = h->harr[h->heap_size - 1];
    h->heap_size--;
    MinHeapify(h, 0);
  }

  printf("Removed :: value %d at index %d\n", val, i);
}

// A recursive method to heapify a subtree with root at given index
void MinHeapify(struct MinHeap *h, int i)
{
  if (h->heap_size <= 31) printTree(h);

  int l = left(i);
  int r = right(i);
  int smallest = i;

  if (l < h->heap_size && h->harr[l] < h->harr[i])
      smallest = l;
  if (r < h->heap_size && h->harr[r] < h->harr[smallest])
      smallest = r;
  if (smallest != i)
  {
      swap(&h->harr[i], &h->harr[smallest]);
      MinHeapify(h, smallest);
  }
}

// A utility function to swap two elements
void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void printHeap(struct MinHeap *h)
{
  if (h == NULL || h->heap_size == 0)
  {
    printf("Heap is empty.\n");
    return;
  }

  for (int i = 0; i < h->heap_size; i++)
  {
    printf("%d ", h->harr[i]);
  }
  printf("\n");
}

// Recursive helper to print the tree sideways
void printTreeHelper(struct MinHeap *h, int index, int space)
{
    // Base case: Stop if index is out of bounds
    if (index >= h->heap_size) return;

    // Increase distance between levels
    space += 5;

    // Process right child first (prints at the top)
    printTreeHelper(h, right(index), space);

    // Print current node after spacing
    printf("\n");
    for (int i = 5; i < space; i++) 
    {
        printf(" ");
    }
    printf("%d\n", h->harr[index]);

    // Process left child (prints at the bottom)
    printTreeHelper(h, left(index), space);
}

void printTree(struct MinHeap *h)
{
  if (h == NULL || h->heap_size == 0)
  {
    printf("Heap is empty.\n");
    return;
  }

  printf("\n--- Top-Down Heap Tree ---\n\n");

  // Calculate total depth of the heap
  int depth = 0;
  int temp = h->heap_size;
  while (temp > 0)
  {
    depth++;
    temp /= 2;
  }

  int index = 0;
  for (int i = 0; i < depth; i++)
  {
    int level_nodes = 1 << i; // Number of nodes at current level
    int space_between = (1 << (depth - i)) - 1; // Spaces between nodes
    int leading_space = space_between / 2; // Initial offset for the row

    // Print leading spaces
    for (int s = 0; s < leading_space; s++) printf("   ");

    // Print nodes and spaces between them
    for (int j = 0; j < level_nodes && index < h->heap_size; j++)
    {
      printf("%3d", h->harr[index++]);
      for (int s = 0; s < space_between; s++) printf("   ");
    }
    printf("\n\n");
  }
  printf("--------------------------\n");
}

void insertRandom(struct MinHeap *h, int n)
{
  if (!h)
  {
    printf("Error: Heap not created. Use 'create <size>' first.\n");
    return;
  }

  // Seed the random number generator
  srand(time(NULL)); 

  for (int i = 0; i < n; i++)
  {
    int random_val = rand() % 100; // Generates a random number between 0 and 99
    insertKey(h, random_val, false);
  }
}

void print_help() 
{
  printf("\n--- Available Commands ---\n");
  printf("create <size>    : Initialize the min-heap with a specific capacity\n");
  printf("random <val>     : Generate a min-heap with n random numbers\n");
  printf("insert <val>     : Insert a value into the min-heap\n");
  printf("delete <index>   : Delete an index from the min-heap\n");
  printf("kx <Kval> <Xval> : Determine whether the heap contains K elements smaller than X\n");
  printf("min              : Display the minimum value\n");
  printf("extract          : Remove the minimum (root) value\n");
  printf("print            : Display the min-heap as an array\n");
  printf("tree             : Display the min-heap as a tree\n");
  printf("help             : Show this help menu\n");
  printf("exit             : Exit the program\n");
  printf("--------------------------\n");
}

int explore(struct MinHeap *h, int i, int k, int x)
{
  if (k <= 0 || i >= h->heap_size || h->harr[i] >= x)
  {
    return 0;
  }

  int leftSubTree = explore(h, left(i), k - 1, x);
  int rightSubTree = explore(h, right(i), k - 1 - leftSubTree, x);

  return 1 + leftSubTree + rightSubTree;
}

bool kSmallerThanX(struct MinHeap *h, int k, int x)
{
  return explore(h, 0, k, x) >= k;
}

int main()
{
  char input[1024];
  char *args[16];
  struct MinHeap *h = NULL;

  print_help();
  
  while (1)
  {
    printf("heap> ");
    if (!fgets(input, sizeof(input), stdin)) break;

    // Tokenize input
    int argc = 0;
    char *token = strtok(input, " \n");
    while (token && argc < 16) 
    {
      args[argc++] = token;
      token = strtok(NULL, " \n");
    }

    if (argc == 0) continue;

    // Command processing
    if (strcmp(args[0], "exit") == 0)
    {
      break;
    }
    else if (strcmp(args[0], "print") == 0)
    {
      if (!h) printf("Error: Heap not created. Use 'create <size>' first.\n");
      else printHeap(h); 
    }
    else if (strcmp(args[0], "create") == 0 && argc == 2)
    {
      if (h) 
      { 
        free(h->harr); free(h); 
        printf("Old heap destroyed, new empty heap created\n");
      }
      h = createMinHeap(atoi(args[1]));
    }
    else if (strcmp(args[0], "insert") == 0 && argc == 2)
    {
      if (!h) printf("Error: Heap not created. Use 'create <size>' first.\n");
      else insertKey(h, atoi(args[1]),true);
    }
    else if (strcmp(args[0], "delete") == 0 && argc == 2)
    {
      int index = atoi(args[1]);
      if (!h) printf("Error: Heap not created. Use 'create <size>' first.\n");
      else if (index < 0 || index >= h->heap_size) printf("Error: Index out of bounds.\n");
      else deleteKey(h, index);
    }
    else if (strcmp(args[0], "extract") == 0)
    {
      if (!h) printf("Error: Heap not created. Use 'create <size>' first.\n");
      else extractMin(h);
    }
    else if (strcmp(args[0], "min") == 0)
    {
      if (!h) printf("Error: Heap not created. Use 'create <size>' first.\n");
      else if (h->heap_size > 0) printf("%d\n", getMin(h));
      else printf("Error: Heap is empty.\n");
    }
    else if (strcmp(args[0], "help") == 0) 
    {
      print_help();
    }
    else if (strcmp(args[0], "random") == 0 && argc == 2)
    {
      
      int n = atoi(args[1]);
      if (!h) h = createMinHeap(n);
      else 
      { 
        free(h->harr); free(h); 
        h = createMinHeap(n);
        printf("Old heap destroyed, new empty heap created\n");
      }
      printf("Created new heap with capacity %d\n", n);
      insertRandom(h, n);
    }
    else if (strcmp(args[0], "kx") == 0 && argc == 3) 
    {
      int k = atoi(args[1]);
      int x = atoi(args[2]);
      bool result = kSmallerThanX(h, k, x);
      printf("Does this min-heap contain %d elements smaller than %d?\n %s.\n", k, x, result ? "True" : "False");
    }
    else if (strcmp(args[0], "tree") == 0)
    {
      if (!h) printf("Error: Heap not created. Use 'create <size>' first.\n");
      else if (h->heap_size > 31) printf("Error: Heap size (%d) exceeds the maximum printable tree size of 31.\n", h->heap_size);
      else printTree(h);
    }
    else
    {
      printf("Invalid command. Type 'help' for a list of available commands.\n");
    }
  }

  if (h)
  {
    free(h->harr);
    free(h);
  }

  return 0;
}
