# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):

      """
      A better evaluation function that considers:
      - Distance t the closest food (prefer closer food)
      - Distance to ghosts (avoid nearby active ghosts)
      - Avoiding the STOP action
      - Eating scared ghosts if possible
      """

      # generate successor state from the action
      successorGameState = currentGameState.generatePacmanSuccessor(action)
      newPos = successorGameState.getPacmanPosition()
      newFood = successorGameState.getFood()
      newGhostStates = successorGameState.getGhostStates()
      newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
      score = successorGameState.getScore()

      # 1. distance to nearest food (want this to be small)
      foodList = newFood.asList()
        if foodList:
            minFoodDist = min(util.manhattanDistance(newPos, food) for food in foodList)
            score += 10.0 / (minFoodDist + 1)  # reciprocal: closer food → higher score

        # 2. distance to ghosts
        for i, ghost in enumerate(newGhostStates):
            ghostPos = ghost.getPosition()
            dist = util.manhattanDistance(newPos, ghostPos)
            if newScaredTimes[i] == 0:
                # Ghost is dangerous → keep away
                if dist < 2:
                    score -= 100  # strong penalty for being too close to active ghost
                else:
                    score += dist  # reward distance to avoid crowding
            else:
                # Ghost is scared → chase it
                score += 10.0 / (dist + 1)

        # 3. avoid STOP action
        if action == Directions.STOP:
            score -= 5

      return score


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Minimax agent (question 2)
    """

    def getAction(self, gameState):
    """
    Returns the minimax action using self.depth and self.evaluationFunction.
    """

    def minimax(state, depth, agentIndex):
      # base case: game over or depth reached
      if state.isWin() or state.isLose() or depth == self.depth:
          return self.evaluationFunction(state)

      # get total number of agents
      numAgents = state.getNumAgents()

      # if it's Pacman's turn (maximize)
      if agentIndex == 0:
          bestValue = float('-inf')
          for action in state.getLegalActions(agentIndex):
              successor = state.generateSuccessor(agentIndex, action)
              value = minimax(successor, depth, 1)  # move to first ghost
              bestValue = max(bestValue, value)
          return bestValue

      # if it's a ghost's turn (minimize)
      else:
          nextAgent = agentIndex + 1
          if nextAgent == numAgents:
              nextAgent = 0
              depth += 1

          bestValue = float('inf')
          for action in state.getLegalActions(agentIndex):
              successor = state.generateSuccessor(agentIndex, action)
              value = minimax(successor, depth, nextAgent)
              bestValue = min(bestValue, value)
          return bestValue

    # start minimax search — find best action for Pacman
    bestScore = float('-inf')
    bestAction = None
    for action in gameState.getLegalActions(0):
        successor = gameState.generateSuccessor(0, action)
        value = minimax(successor, 0, 1)  # depth 0, first ghost's turn
        if value > bestScore:
            bestScore = value
            bestAction = action

    return bestAction


class AlphaBetaAgent(MultiAgentSearchAgent):
      """
      Minimax agent with alpha-beta pruning (question 3)
    """

  def getAction(self, gameState):
    """
    Returns the minimax action using self.depth and self.evaluationFunction,
    with alpha-beta pruning.
    """
    def alphabeta(state, depth, agentIndex, alpha, beta):
      """
      Recursive helper function implementing alpha-beta pruning.

      state: current GameState
      depth: current depth in the tree
      agentIndex: index of the agent whose turn it is (0 = Pacman, >=1 = ghosts)
      alpha: best already explored option along the path to the root for max
      beta: best already explored option along the path to the root for min
      """
      # terminal state or maximum search depth reached
      if state.isWin() or state.isLose() or depth == self.depth:
          return self.evaluationFunction(state)
      numAgents = state.getNumAgents()

      # Pacman's turn (Max)
      if agentIndex == 0:
          value = float('-inf')
          for action in state.getLegalActions(agentIndex):
              successor = state.generateSuccessor(agentIndex, action)
              # recursive call to next agent (first ghost)
              value = max(value, alphabeta(successor, depth, 1, alpha, beta))
              # prune: if value is already worse than beta, stop
              if value > beta:
                  return value
              alpha = max(alpha, value)
          return value

      # Ghost's turn (Min)
      else:
          nextAgent = agentIndex + 1
          if nextAgent == numAgents:
            # all agents moved, increment depth and return to Pacman
              nextAgent = 0
              depth += 1

          value = float('inf')

          for action in state.getLegalActions(agentIndex):
              successor = state.generateSuccessor(agentIndex, action)
              # recursive call to next agent or Pacman
              value = min(value, alphabeta(successor, depth, nextAgent, alpha, beta))
              # prune: if value is already worse than alpha, stop
              if value < alpha:
                  return value
              beta = min(beta, value)
          return value

    # root call: Pacman moves first
    alpha = float('-inf') # best value so far for Pacman (max)
    beta = float('inf')   # best value so far for Ghosts (min)
    bestScore = float('-inf')
    bestAction = None

    # evaluate all legal actions Pacman can take
    for action in gameState.getLegalActions(0):
        successor = gameState.generateSuccessor(0, action)
        value = alphabeta(successor, 0, 1, alpha, beta)
        if value > bestScore:
            bestScore = value
            bestAction = action
        # update alpha with best so far
        alpha = max(alpha, bestScore)

    return bestAction


class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)

    This agent assumes that ghosts move randomly (not adversarially).
    Instead of minimizing, ghost nodes use an expectation over possible outcomes.
  """

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction.

      All ghosts are modeled as choosing uniformly at random from their legal moves.
    """

    def expectimax(state, depth, agentIndex):
      """
        Recursive helper function implementing the Expectimax algorithm.

        state: current GameState
        depth: current depth in the tree
        agentIndex: index of the current agent (0 = Pacman, >=1 = ghosts)
      """
      # base case: terminal state or max depth reached
      if state.isWin() or state.isLose() or depth == self.depth:
          return self.evaluationFunction(state)

      numAgents = state.getNumAgents()

      # Pacman's turn (Max)
      if agentIndex == 0:
          value = float('-inf')
          for action in state.getLegalActions(agentIndex):
              successor = state.generateSuccessor(agentIndex, action)
              # recursively evaluate the ghost's move next (agentIndex = 1)
              value = max(value, expectimax(successor, depth, 1))
          return value

      # Ghost's turn (Chance node)
      else:
          nextAgent = agentIndex + 1
          if nextAgent == numAgents:
            # all agents moved; go back to Pacman and increment depth
              nextAgent = 0
              depth += 1

          actions = state.getLegalActions(agentIndex)
          if not actions:
            # no legal actions, treat as terminal
              return self.evaluationFunction(state)
          total = 0

          # each ghost move is equally likely (uniform distribution)
          for action in actions:
              successor = state.generateSuccessor(agentIndex, action)
              total += expectimax(successor, depth, nextAgent)

          # return the average (expected) value of all outcomes
          return total / len(actions)

    # initial call: Pacman chooses the best action 
    bestScore = float('-inf')
    bestAction = None
    for action in gameState.getLegalActions(0):
        successor = gameState.generateSuccessor(0, action)
        value = expectimax(successor, 0, 1) # depth = 0, next agent is first ghost
        if value > bestScore:
            bestScore = value
            bestAction = action
    return bestAction


def betterEvaluationFunction(currentGameState):
    """
    A refined evaluation function for Pacman.

    This function considers:
    - Winning and losing states
    - Distance to scared and active ghosts
    - Distance to food
    - Number of remaining food dots
    - Number and distance to capsules
    - Game score

    Goal: Encourage Pacman to eat food, chase scared ghosts,
    avoid active ghosts, and complete the game quickly and safely.
    """

    # scoring Constants
    WIN_BONUS              =  1e9
    LOSE_PENALTY           = -1e9
    GHOST_DANGER_PENALTY   = -500
    SCARED_GHOST_REWARD    = 200
    FOOD_DIST_REWARD       = 10
    FOOD_COUNT_PENALTY     = -4
    CAPSULE_COUNT_PENALTY  = -20

    pos = currentGameState.getPacmanPosition()
    foodList = currentGameState.getFood().asList()
    ghostStates = currentGameState.getGhostStates()
    scaredTimers = [ghost.scaredTimer for ghost in ghostStates]
    capsules = currentGameState.getCapsules()

    # base score 
    score = currentGameState.getScore()

    # handle win/lose 
    if currentGameState.isWin():
        return WIN_BONUS
    if currentGameState.isLose():
        return LOSE_PENALTY

    #  ghost handling 
    for i, ghost in enumerate(ghostStates):
        ghostPos = ghost.getPosition()
        dist = util.manhattanDistance(pos, ghostPos)

        if scaredTimers[i] > 0:
            # Scared ghost: chase it
            score += max(10, SCARED_GHOST_REWARD - 10 * dist)
        elif dist <= 1:
            # Active ghost: avoid it if adjacent
            score += GHOST_DANGER_PENALTY

    # food handling 
    if foodList:
        foodDistances = [util.manhattanDistance(pos, food) for food in foodList]
        minFoodDist = min(foodDistances)
        score += FOOD_DIST_REWARD / (minFoodDist + 1)
        score += len(foodList) * FOOD_COUNT_PENALTY

    # capsule handling 
    score += len(capsules) * CAPSULE_COUNT_PENALTY

    return score
