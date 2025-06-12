## Overview

This project implements a **Value Iteration Agent** for solving Markov Decision Processes (MDPs) using the value iteration algorithm. The goal is to compute optimal policies for different environments such as Gridworld.

---

## Task 1: Value Iteration Implementation

Changes Made in `ValueIterationAgent`:

#### 1. Value Iteration Loop (`__init__`)
* Implemented a batch-style value iteration loop.
* For each (k) iteration:
  * Created a new Counter (`new_values`) to hold updated state values.
  * For each state:
    * Skipped terminal states (no future rewards to consider).
    * Computed Q-values for all legal actions.
    * Set the state’s new value to the maximum Q-value.
* Replaced `self.values` with `new_values` after processing all states.

#### 2. `computeQValueFromValues(state, action)`
* Implemented the Bellman Q-value computation
* For the given state and action:
  * Iterated over all possible (nextState, probability) pairs.
  * Calculated the expected return using current value estimates (self.values).
  * Summed these to produce the Q-value.

#### 3. `computeActionFromValues(state)`
* Returned the action with the highest Q-value for the given state, based on current value estimates (`self.values`).
* Iterated through all legal actions, computed each action's Q-value using `computeQValueFromValues`, and selected the best.
* Returned None if the state is terminal (i.e. no legal actions available).

###  Reason
Compute the optimal value function and policy for a known MDP using value iteration, which applies the Bellman update iteratively. This agent is an example of offline planning in reinforcement learning, where the agent uses a known model of the environment (transition probabilities and rewards) to derive the best policy without interacting with the environment.

---

## Task 2: Bridge Crossing Analysis

##  Parameter Chosen
```python
answerDiscount = 0.9
answerNoise = 0.0
```

###  Reason

* Default noise of 0.2 makes the bridge crossing too risky.
* Setting noise to 0.0 removes randomness in movement.
* This allows the agent to reliably cross the narrow bridge and reach the high-reward state.

---

## Task 3: DiscountGrid Behavior Tuning

###  Functions Implemented

Each function returns a tuple of (`discount`, `noise`, `livingReward`) to produce the desired behavior in the Gridworld environment.

| Function     | Behavior Goal                    | Params            |
| ------------ | -------------------------------- | ----------------- |
| `question3a` | Take close exit, risk cliff      | `0.1, 0.0, -0.1`  |
| `question3b` | Take close exit, avoid cliff     | `0.3, 0.2, -0.1`  |
| `question3c` | Take distant exit, risk cliff    | `0.9, 0.0, 0.0`   |
| `question3d` | Take distant exit, avoid cliff   | `0.9, 0.2, -0.05` |
| `question3e` | Avoid all exits and live forever | `0.9, 0.0, 1.0`   |

###  Reason

Each set of parameters is chosen to balance:

* Long vs. short-term reward focus (`discount`)
* Risk tolerance (`noise`)
* Incentive to keep moving or to terminate early (`livingReward`)

