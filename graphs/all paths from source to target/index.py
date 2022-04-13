'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
 

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.
'''

'''
nodes are labeled from 0 to n - 1. (increasing order from 0... n-1)
dfs with backtracking and global output set. so we try to get to n-1,
we dfs and have a "banned" set that we add to and remove from once we visited
graph basically gives us neighbors to go through
let's first make a dictionary with
{
    node: set(neighbors)
}

# make a copy of the array so it doesn't change by reference
set does not preserve order so need to have a set for faster access AND an array to preserve order
copy the array and add it to output so it doesn't change by reference

time - O(n^2?) or O(n)
space O(n) for set, and array
'''

from typing import List, Dict, OrderedDict, Set, Tuple
from collections import defaultdict

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dict = defaultdict(set)       
        output = (len(graph) - 1, []) # n-1 and answer
        # use a set for faster access and list to preserve order
        visited = (set(), [])
        for i in range(len(graph)):
            # node: set(neighbors)
            for neighbor in graph[i]:
                dict[i].add(neighbor)

        # print('dict', dict)
        

        def helper(cur: int, dict: Dict[int, Set[int]], visited: Tuple[Set[int], List[int]], output: Tuple[int, List[List[int]]]) -> None:
            if cur == output[0]:
                # make a copy of the array so it doesn't change by reference
                copyVisited = visited[1].copy()
                output[1].append(copyVisited)
                # assuming n-1 doesn't direct to anywhere else
                return
            for neighbor in dict[cur]:
                if neighbor not in visited[0]:
                    visited[0].add(neighbor), visited[1].append(neighbor)
                    

                    # print('cur', cur, 'neighbor', neighbor)

                    helper(neighbor, dict, visited, output)
                    visited[0].remove(neighbor), visited[1].remove(neighbor)
            
        
        visited[0].add(0), visited[1].append(0)
        helper(0, dict, visited, output)
        return output[1]


# sol = Solution()
# output = sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])
# print(output)
