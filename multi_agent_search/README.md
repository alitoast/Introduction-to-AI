## Overview

This project extends Pacman AI by implementing multi-agent search algorithms to handle adversarial and stochastic environments with multiple ghosts. The goal is to create agents that can plan and act optimally or near-optimally by considering the behaviors of other agents (ghosts) and the stochasticity of the environment.

---

## Key Implementations and Changes

### 1. **Reflex Agent Enhancement**

* Improved the reflex agent’s evaluation function to incorporate both **food locations** and **ghost positions**, rewarding proximity to food while avoiding dangerous ghosts.
* Used reciprocal distances to food and ghosts to provide more informative feedback for decision-making.

### 2. **Minimax Agent**

* Implemented the **Minimax algorithm** supporting multiple ghost agents as minimizers.
* Enabled arbitrary search depth with recursive evaluation, considering all agents’ moves in sequence.
* Pacman (agent 0) acts as the maximizing player, ghosts act as minimizers.

### 3. **Alpha-Beta Pruning**

* Extended the minimax agent to use **alpha-beta pruning**, improving efficiency by pruning branches that cannot influence the final decision.
* Maintained correctness while significantly reducing the search tree size and improving runtime performance.

### 4. **Expectimax Agent**

* Developed an **Expectimax agent** modeling ghosts as stochastic agents that choose their moves uniformly at random.
* Expected value calculations replace minimax’s worst-case assumptions, better modeling uncertain ghost behavior.

### 5. **Better Evaluation Function**

* Designed a comprehensive evaluation function that combines:

  * Distance to the closest food pellet.
  * Active ghost avoidance (heavy penalties for close active ghosts).
  * Opportunity to chase scared ghosts.
  * Remaining food and capsule counts.
* This heuristic encourages survival, effective food collection, and strategic use of power capsules.

---

## Why These Changes?

* **Handling multiple agents:** Realistic Pacman gameplay involves several adversaries (ghosts). The multi-agent search algorithms model these interactions explicitly.
* **Efficiency:** Alpha-beta pruning ensures the search remains computationally feasible at greater depths.
* **Uncertainty:** Expectimax accounts for randomness in ghost movements, better reflecting actual game dynamics.
* **Balanced decision-making:** The better evaluation function guides Pacman to balance between collecting food and avoiding danger.

---

## How to Use

* Run each agent by specifying the agent type in the command line (e.g., `-p MinimaxAgent`, `-p AlphaBetaAgent`, `-p ExpectimaxAgent`).
* Adjust search depth and evaluation functions via command line arguments or configuration settings.
* Use flags like `-f` for fixed random seeds or `-q` to disable graphics and speed up simulations.

