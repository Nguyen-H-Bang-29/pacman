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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    backtrackingPath = []
    foundGoal = False
    visited = [problem.getStartState()]

    def move(actionDone, backtrackingPath, foundGoal, visited):
        if problem.isGoalState(actionDone[0]):
            return actionDone[1]
        else:
            visited.append(actionDone[0])
        
        for action in problem.getSuccessors(actionDone[0]):
            next = None
            if action[0] not in visited:
                next = move(action, backtrackingPath, foundGoal, visited)
            if(next != None):
                backtrackingPath.append(next)
                return actionDone[1]
        
        return None

    for action in problem.getSuccessors(problem.getStartState()):
        next = None
        if action[0] not in visited:
            next = move(action, backtrackingPath, foundGoal, visited)
        if(next != None):
            backtrackingPath.append(next)
            break
    
    return backtrackingPath[::-1]
    


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    # init queue, keep track of action chain and cummulated cost to achieve state
    queue.push((problem.getStartState(), [], []))
    visited = [problem.getStartState()]

    while not queue.isEmpty():
        state, actions, cost = queue.pop()
        if problem.isGoalState(state): return actions
        for successor in problem.getSuccessors(state):
            if successor[0] in visited: continue
            visited.append(successor[0])
            queue.push((successor[0], actions + [successor[1]], cost + [successor[2]]))
    return []
    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    heap = util.PriorityQueue()
    heap.push((problem.getStartState(), [], []), 0)
    visited = []
    while not heap.isEmpty():
        state, actions, cost = heap.pop()
        if state in visited: continue
        if problem.isGoalState(state): return actions
        for successor in problem.getSuccessors(state):
            if successor[0] in visited: continue
            heap.push((successor[0], actions + [successor[1]], problem.getCostOfActions(actions + [successor[1]])), problem.getCostOfActions(actions + [successor[1]]))
        visited.append(state)
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    heap = util.PriorityQueue()
    heap.push((problem.getStartState(), [], []), heuristic(problem.getStartState(), problem))
    visited = []
    while not heap.isEmpty():
        state, actions, cost = heap.pop()
        if state in visited: continue
        if problem.isGoalState(state): return actions
        for successor in problem.getSuccessors(state):
            if successor[0] in visited: continue
            heap.push((successor[0], actions + [successor[1]], problem.getCostOfActions(actions + [successor[1]])), problem.getCostOfActions(actions + [successor[1]]) + heuristic(successor[0], problem))
        visited.append(state)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
