## Overview

This project implements a **Value Iteration Agent** for solving Markov Decision Processes (MDPs) using the value iteration algorithm. The goal is to compute optimal policies for different environments such as Gridworld.

This README describes the changes made in:
- `valueIterationAgents.py` (Task 1)
- `analysis.py` (Tasks 2 & 3)

---

## Task 1: Value Iteration Implementation

**File Modified**: `valueIterationAgents.py`

**Class Implemented**: `ValueIterationAgent`

### ✅ Changes Made

#### 1. Value Iteration Loop (`__init__`)
- Implemented a batch-style value iteration loop.
- For each iteration:
  - Copied previous values.
  - For each state, computed the max Q-value from all legal actions.
  - Updated state values using those max Q-values.
- Handled terminal states by skipping value updates.

#### 2. `computeQValueFromValues(state, action)`
- Computed Q(s, a) using:
  
```
Q(s,a) = Σ \[P(s'|s,a) \* (R(s,a,s') + γ \* V(s'))]

```

- Used the transition model and rewards provided by the MDP.

#### 3. `computeActionFromValues(state)`
- Returned the action that yielded the maximum Q-value from the current state's value.
- Returned `None` for terminal states.

###  Reason
To compute an optimal value function and policy using the Bellman update. Implementing this agent demonstrates the core planning loop in reinforcement learning.

---

## Task 2: Bridge Crossing Analysis

**File Modified**: `analysis.py`

**Function Implemented**: `question2()`

###  Parameter Chosen
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

**File Modified**: `analysis.py`

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

