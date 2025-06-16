# Overview

This project demonstrates how different uninformed search algorithms can be used by Pacman to navigate a maze and find a fixed food dot. The algorithms implemented include:

* **Depth-First Search (DFS)**
* **Breadth-First Search (BFS)**
* **Uniform Cost Search (UCS)**

Each function explores the maze in a different way and returns a sequence of actions for Pacman to reach the goal.

---

##  Implemented Algorithms

### 1. **Depth-First Search (DFS)**

* **Strategy:** Explores as far as possible along each branch before backtracking.
* **Fringe Structure:** LIFO Stack.
* **Behavior:** Goes deep first; may find suboptimal solutions if costs vary.
* **Implementation Highlights:**

  * Uses a set to track visited states.
  * Appends successors to the stack.

### 2. **Breadth-First Search (BFS)**

* **Strategy:** Explores all neighbors before going deeper.
* **Fringe Structure:** FIFO Queue.
* **Behavior:** Guarantees the shortest path (in steps), assuming uniform cost.
* **Implementation Highlights:**

  * Uses a set to avoid revisiting states.
  * Pushes successors level by level.

### 3. **Uniform Cost Search (UCS)**

* **Strategy:** Always expands the node with the lowest total path cost.
* **Fringe Structure:** Priority Queue ordered by cumulative cost.
* **Behavior:** Finds the **least-cost path**, accounts for different step costs.
* **Implementation Highlights:**

  * Stores visited states with the minimum cost found so far.
  * Expands successors with updated cumulative cost.

---

## Observations

* **DFS** may return a longer or suboptimal path due to its depth bias.
* **BFS** ensures the shortest path in number of steps.
* **UCS** finds the cheapest path considering cost, and is ideal when movement costs vary.
