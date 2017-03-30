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
import node
import sets

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
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    root_node = node.Node(problem.getStartState())

    frontier = util.Stack()
    frontier.push(root_node)
    explored = sets.Set()
    end_node = None

    while not frontier.isEmpty():

        # choose a leaf node and remove it from the frontier
        leaf_node = frontier.pop()

        # if the node contains a goal state then return the corresponding solution
        if problem.isGoalState(leaf_node.get_state()):
            end_node = leaf_node
            break

        # add the node to the explored set
        explored.add(leaf_node)

        # expand the chosen node, adding the resulting nodes to the frontier
        for successor, action, cost in problem.getSuccessors(leaf_node.get_state()):

            child_node = node.Node(successor)
            child_node.set_parent(leaf_node)
            child_node.set_action(action)
            child_node.add_cost(cost)

            # TODO: if checking child node in frontier this fails, if not (child_node in explored or child_node in frontier):
            if not (child_node in explored):
                frontier.push(child_node)

    return end_node.path()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    root_node = node.Node(problem.getStartState())
    frontier = util.Queue()
    frontier.push(root_node)
    explored = sets.Set()
    end_node = None

    while not frontier.isEmpty():

        # choose a leaf node and remove it from the frontier
        leaf_node = frontier.pop()

        # if the node contains a goal state then return the corresponding solution
        if problem.isGoalState(leaf_node.get_state()):
            end_node = leaf_node
            break

        # add the node to the explored set
        explored.add(leaf_node)

        # expand the chosen node, adding the resulting nodes to the frontier
        for successor, action, cost in problem.getSuccessors(leaf_node.get_state()):

            child_node = node.Node(successor)
            child_node.set_parent(leaf_node)
            child_node.set_action(action)
            child_node.add_cost(cost)

            if not (child_node in explored or child_node in frontier):
                frontier.push(child_node)

    return end_node.path()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    root_node = node.Node(problem.getStartState())
    frontier = util.PriorityQueue()
    frontier.push(root_node, 0)
    explored = sets.Set()
    end_node = None

    while not frontier.isEmpty():
        # choose a leaf node and remove it from the frontier
        leaf_node = frontier.pop()

        # if the node contains a goal state then return the corresponding solution
        if problem.isGoalState(leaf_node.get_state()):
            end_node = leaf_node
            break

        # add the node to the explored set
        explored.add(leaf_node)

        # expand the chosen node, adding the resulting nodes to the frontier
        for successor, action, cost in problem.getSuccessors(leaf_node.get_state()):

            child_node = node.Node(successor)
            child_node.set_parent(leaf_node)
            child_node.set_action(action)
            child_node.add_cost(cost)
            child_node.add_cost(leaf_node.get_cost())

            if not (child_node in explored or child_node in frontier):
                frontier.push(child_node, child_node.get_cost())

            elif child_node in frontier:
                frontier.update(child_node, child_node.get_cost())

    return end_node.path()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
