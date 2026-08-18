# Data Structures and Algorithms in Python

This course section introduces core data structures and algorithms through
Jupyter notebooks. The examples favor readability and step-by-step output so
you can see how each structure changes as operations run.

## Recommended Order

1. `implementing_data_structures/time_complexity.ipynb`
2. `implementing_data_structures/stack.ipynb`
3. `implementing_data_structures/queue.ipynb`
4. `implementing_data_structures/linked_list.ipynb`
5. `implementing_sorting_algorithms/sorting.ipynb`
6. `implementing_trees_and_graphs/binary_search.ipynb`
7. `implementing_trees_and_graphs/binary_tree.ipynb`
8. `implementing_trees_and_graphs/graph.ipynb`
9. `implementing_trees_and_graphs/graph_traversal.ipynb`
10. `implementing_trees_and_graphs/topological_sort.ipynb`

## Topic Map

| Topic | Files | Main ideas |
| --- | --- | --- |
| Time complexity | `time_complexity.ipynb` | Big O, constant time, linear scans, nested loops |
| Stack | `stack.ipynb` | LIFO, `push`, `pop`, `peek`, underflow |
| Queue | `queue.ipynb` | FIFO, standard-library queue, custom queue |
| Linked list | `linked_list.ipynb` | Nodes, head pointer, append, prepend, remove, reverse |
| Sorting | `sorting.ipynb` | Selection, bubble, insertion, shell, merge, quick sort |
| Binary search | `binary_search.ipynb` | Sorted input, midpoint search, O(log n) |
| Binary tree | `binary_tree.ipynb` | BST insert, lookup, min/max, BFS, DFS |
| Graphs | `graph.ipynb`, `graph.py` | Interfaces, adjacency sets, adjacency matrices |
| Graph traversal | `graph_traversal.ipynb` | Breadth-first search, depth-first search |
| Topological sort | `topological_sort.ipynb` | DAGs, indegree, dependency ordering |

## Use Cases

- Use stacks for undo/redo history, expression parsing, browser navigation, and
  recursive problem tracing.
- Use queues for task scheduling, event processing, producer/consumer flows,
  and breadth-first traversal.
- Use linked lists when frequent insertion/removal near known nodes matters
  more than random access.
- Use sorting before reporting, ranking, binary searching, deduplicating, or
  merging datasets.
- Use binary search for fast lookup in sorted arrays, search spaces, and
  threshold-finding problems.
- Use binary search trees for ordered data when insert, lookup, min, max, and
  sorted traversal are all important.
- Use graphs for networks, maps, dependencies, workflows, social connections,
  and recommendation paths.
- Use topological sort when tasks must be ordered by prerequisites.

## Practice Labs

1. Time complexity: add a new function with one loop and one nested loop, then
   predict the Big O before running it.
2. Stack: add a `clear()` method and test that `is_empty()` returns true after
   clearing.
3. Queue: update `MyQueue.dequeue()` to raise a custom message when the queue is
   empty.
4. Linked list: implement a `find()` method that returns the matching node or
   `None`, then test a found and missing value.
5. Linked list: add `insert_before(target, value)` and test inserting before the
   head and before a middle node.
6. Sorting: count comparisons and swaps for each sorting algorithm on the same
   input list.
7. Sorting: run each sort on an already sorted list and a reverse-sorted list,
   then compare the printed steps.
8. Binary search: return the index of the found value instead of only printing a
   message.
9. Binary tree: add a `height()` function and test it after inserting more
   nodes.
10. Tree traversal: explain why in-order traversal of this BST returns sorted
    values.
11. Graphs: create the same graph using both adjacency-set and adjacency-matrix
    representations, then compare outputs.
12. Graph traversal: start BFS and DFS from different vertices and record the
    visit order.
13. Topological sort: build a course-prerequisite graph and verify prerequisites
    appear before dependent courses.

## Challenge Extensions

- Replace the list-backed queue with `collections.deque` and compare
  `dequeue()` complexity.
- Improve prime checking by testing divisors only up to the square root of the
  number.
- Add cycle detection to topological sort so it reports when no valid ordering
  exists.
- Add type hints to the custom stack, queue, linked list, and tree classes.
- Write small unit tests for each custom data structure outside the notebooks.

## Quick Complexity Reference

| Pattern | Typical Big O | Example in this course |
| --- | --- | --- |
| Direct arithmetic or condition | O(1) | Addition, odd/even check |
| One loop over input | O(n) | Find maximum, factorial |
| Binary halving | O(log n) | Binary search |
| Nested loop over same input | O(n^2) | Print all pairs |
| Divide and conquer sort | O(n log n) | Merge sort, average quick sort |
| Matrix graph storage | O(V^2) space | Adjacency matrix |
| Neighbor-set graph storage | O(V + E) space | Adjacency set |

## Notes for Learners

The code is written for instruction, so some implementations are intentionally
simple instead of fully production-ready. When a cell raises an error, read the
message and inspect the state that caused it. Understanding failure cases is a
major part of learning data structures.

