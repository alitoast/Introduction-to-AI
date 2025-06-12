## Overview

This project implements various AI agents to play Pacman using different search and decision-making algorithms. The main focus is on improving the Reflex Agent, implementing Minimax, Alpha-Beta pruning, Expectimax, and crafting a better evaluation function.

---

## Changes and Implementations

### 1. **ReflexAgent Enhancement**

* **What was done:**
  The ReflexAgent’s evaluation function was improved to consider both the **distance to food** and the **proximity to ghosts**. Instead of only using the successor game score, the evaluation also penalizes positions near active ghosts to avoid death, and rewards being closer to food, encouraging more strategic and safer moves.

* **Why:**
  The original reflex agent was myopic, focusing mainly on the score and immediate food. By adding ghost distance and food proximity features, the agent can better balance risk and reward, improving survival and efficiency in collecting food.

---

### 2. **MinimaxAgent Implementation**

* **What was done:**
  Implemented a full minimax search algorithm that handles multiple ghosts by treating each ghost as a separate minimizing agent. The depth of search and the evaluation function are configurable parameters.

* **Why:**
  Minimax allows Pacman to plan ahead by considering the best possible outcome assuming adversarial ghost behavior. Handling multiple ghosts in the tree is essential for realistic gameplay.

---

### 3. **AlphaBetaAgent Implementation**

* **What was done:**
  Added alpha-beta pruning to the minimax agent to prune branches that cannot affect the final decision, improving efficiency without sacrificing optimality.

* **Why:**
  Alpha-beta pruning significantly reduces the number of nodes explored, making the agent faster and more scalable, especially for deeper search depths or larger maps.

---

### 4. **ExpectimaxAgent Implementation**

* **What was done:**
  Implemented the expectimax algorithm where ghosts are modeled as stochastic agents choosing moves uniformly at random. The agent computes expected values over ghost moves rather than worst-case outcomes.

* **Why:**
  Expectimax better models real ghost behavior when ghosts are not fully adversarial but instead act randomly. This often leads to more realistic and sometimes more effective decision-making.

---

### 5. **Better Evaluation Function**

* **What was done:**
  Developed a more sophisticated evaluation function that combines:

  * Distance to the closest food pellet (encouraging Pacman to chase food).
  * Ghost proximity: large penalty for ghosts that are near and active; rewards chasing scared ghosts.
  * Number of remaining food pellets and capsules (incentivizing eating pellets and power capsules).

* **Why:**
  The default scoring function often fails to capture the trade-offs between survival and scoring. This improved heuristic guides Pacman to both stay alive and aggressively collect food and power-ups.
