'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
'''

'''
need a course_to_prereq
course: pre-requisite course
{
    0: 1
}
go from 0->n-1 and check what courses don't have pre-req and subtract that from numCourses
return numCourses == 0

{
    1: 0,
    0: 1
}
visited so we don't go in loops
Set[int]
'''

'''
if inorder to take course 0 you have to take course 1 and this is represented by a pair (or EDGE)
[0, 1]
0 <- 1
directed graph 
is it possible to take course 0? 0 doesn't have any outward edges from 0,
so it is possible for us to complete course 0 
then we look at course 1, it does have 1 pre-requisite, it is course 0
and we know course 0 is possible to complete so once we complete course 0 we can take course 1

impossible prereq = [[1,0], [0,1]]

1 <- 0
  ->
we have a cycle. in this case we return False

DFS
first visualize it and draw directed graph with outward edges
no pre-reqs are our base cases where we start from
we don't need a graph to tell us that.
we can use a data structure called an adjacency list
it will be called prerequisiteMap because the data structure used is a hashmap
for each of our courses we will have a list of all it's prerequisites
prereq = [[0,1],[0,2],[1,3],[1,4],[3,4]]
        preMap
course          pre
0               1,2
1               3,4
2                []
3                4
4                []

course 4 we can complete
then recursively 3 we can complete because 4 is completed
then from 1 we know 3 can be completed and check 4, 4 can be completed so 1 can be completed
then back to 0 we know 1 can be completed and see 2 can be completed
therefore we know 0 can be completed

how do we detect a loop? use a visit set
say we start at 0 and add 0 to our vistSet
then add 1 once we reach there. we see that we reach 0 again that is in visitSet so it detects a loop

time complexity O(n + p). n = node, p = prereqs
space O(n) for hashmap

remember to remove from visit set once we visit all the course's pre
to make it faster, we know we can visit the course at the end so we set it's premap[course] = []
# we have to iterate through every course and check, in case we have this:
# 1->2, 3->4
'''

from typing import Dict, List, Set

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        # visitSet = all courses along the curr DFS path
        visitSet = set()
        def helper(course: int) -> bool:
            if course in visitSet:
                return False
            if preMap[course] == []:
                return True
            
            visitSet.add(course)
            # loop through all pre for course
            for pre in preMap[course]:
                if not helper(pre):
                    return False
            visitSet.remove(course)
            preMap[course] = []
            return True
        
        # we have to iterate through every course and check, in case we have this:
        # 1->2, 3->4
        for course in range(numCourses):
            if not helper(course):
                return False
        return True


# sol = Solution()
# output = sol.canFinish(3, [[1,0],[1,2],[0,1]])
# print(output)