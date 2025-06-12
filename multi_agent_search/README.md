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


### 4. **Expectimax Agent**

* Developed an **Expectimax agent** modeling ghosts as stochastic agents that choose their moves uniformly at random.


### 5. **Better Evaluation Function**

This evaluation function is designed to guide Pacman toward aggressive yet safe play. It encourages Pacman to quickly collect food, opportunistically chase scared ghosts, and avoid dangerous encounters.
It considers multiple aspects of the current game state to compute a heuristic score:

* **Game Outcome:** Rewards winning states and heavily penalizes losing ones.
* **Ghost Awareness:**

  * Strongly penalizes being adjacent to active (non-scared) ghosts.
  * Rewards chasing scared ghosts, with preference for closer ones.
* **Food Prioritization:**

  * Encourages moving toward the nearest food pellet.
  * Penalizes the total number of remaining food dots.
* **Capsule Strategy:**

  * Penalizes the number of remaining power capsules to encourage collecting them.
* **Game Score:** Includes the actual game score as part of the evaluation.