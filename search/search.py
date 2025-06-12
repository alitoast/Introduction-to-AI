# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack
from game import Directions
from collections import deque

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Implements depth-first search (DFS) using a LIFO stack to explore
    the deepest nodes in the search tree first.

    Returns:
        A list of actions that reaches the goal state.
    """

    # use a stack to manage the fringe (nodes to explore)
    fringe = Stack()
    visited = set()

    # push the start state and an empty path
    start_state = problem.getStartState()
    fringe.push((start_state, []))

    while not fringe.isEmpty():
        current_state, path = fringe.pop()

        # if we reach the goal, return the path
        if problem.isGoalState(current_state):
            return path

        # only expand unvisited nodes
        if current_state not in visited:
            visited.add(current_state)

            # add all successors to the stack with updated paths
            for successor, action, cost in problem.getSuccessors(current_state):
                new_path = path + [action]
                fringe.push((successor, new_path))

    return []  # no path found



def breadthFirstSearch(problem):
    """
    Implements breadth-first search (BFS) using a FIFO queue.
    Explores the shallowest unexpanded nodes first.

    Returns:
        A list of actions that reaches the goal state.
    """

    # use a queue to explore nodes level by level
    frontier = util.Queue()
    visited = set()

    # push the start state and an empty path
    frontier.push((problem.getStartState(), []))

    while not frontier.isEmpty():
        state, path = frontier.pop()

        # if we reach the goal, return the path
        if problem.isGoalState(state):
            return path

        # expand only unvisited nodes
        if state not in visited:
            visited.add(state)

            # enqueue successors with updated paths
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in visited:
                    frontier.push((successor, path + [action]))

    return []  # no path found



def uniformCostSearch(problem):
    """
    Implements Uniform Cost Search (UCS), expanding the node with the
    lowest cumulative cost from the start state.

    Returns:
        A list of actions that reaches the goal state with minimal cost.
    """

    # priorityQueue orders nodes by path cost
    frontier = util.PriorityQueue()
    visited = {}

    # push start state with cost 0
    frontier.push((problem.getStartState(), [], 0), 0)

    while not frontier.isEmpty():
        state, path, cost = frontier.pop()

        # skip if already visited with a cheaper cost
        if state in visited and visited[state] <= cost:
            continue

        visited[state] = cost

        # goal check
        if problem.isGoalState(state):
            return path

        # push successors with updated cumulative cost
        for successor, action, stepCost in problem.getSuccessors(state):
            newCost = cost + stepCost
            frontier.push((successor, path + [action], newCost), newCost)

    return []  # no path found



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Implements A* Search combining UCS with a heuristic estimate
    of remaining cost to the goal.

    Returns:
        A list of actions that reaches the goal efficiently.
    """

    frontier = util.PriorityQueue()
    visited = {}

    start_state = problem.getStartState()
    start_cost = 0
    start_priority = start_cost + heuristic(start_state, problem)
    frontier.push((start_state, [], start_cost), start_priority)

    while not frontier.isEmpty():
        state, path, cost = frontier.pop()

        # skip if visited with lower or equal cost
        if state in visited and visited[state] <= cost:
            continue

        visited[state] = cost

        # goal check
        if problem.isGoalState(state):
            return path

        # evaluate successors with heuristic
        for successor, action, step_cost in problem.getSuccessors(state):
            new_cost = cost + step_cost
            priority = new_cost + heuristic(successor, problem)
            frontier.push((successor, path + [action], new_cost), priority)

    return []  # no path found



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
