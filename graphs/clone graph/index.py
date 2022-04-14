'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
 

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
'''

'''
base case

class Node {
    public int val;
    public List<Node> neighbors; -> List of nodes
                                ie. [<__main__.Node object at 0x7f17c4c96530>, <__main__.Node object at 0x7f17c4c96aa0>]
}

no self loops, no reppeated edges and each value is unique

get node's val and add to visited set
dfs and for loop into each neighbor
if not visited keep going? and set neighbor and value
visited will be a dictionary of value(int) to new Node created
or Node: Node

O(n) time - n is number of nodes
O(n) space - for dictionary
'''


# Definition for a Node.
from typing import Dict, List, Set


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # base case:
        if node is None:
            return None
        
        
        def helper(new: Node, old: Node, visited: Dict[Node, Node]) -> None:
            
            for neighbor in old.neighbors:
                if neighbor not in visited:
                    # create new neighbor
                    visited[neighbor] = Node(neighbor.val)
                    # visited[neighbor] = newNeighbor
                    helper(visited[neighbor], neighbor, visited)
                # add new neighbor
                new.neighbors.append(visited[neighbor])


        new = Node(node.val)
        visited = {node: new}
        helper(new, node, visited)
        return new