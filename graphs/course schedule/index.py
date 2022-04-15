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

from typing import Dict, List, Set
from xmlrpc.client import Boolean


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create course: pre-requisite course course_to_prereqionary
        self.coursesLeft = numCourses
        course_to_prereq = {}
        prereq_to_course = {}
        for courseRequirement in prerequisites:
            course_to_prereq[courseRequirement[0]] = courseRequirement[1]
            prereq_to_course[courseRequirement[1]] = courseRequirement[0]
        startingCourses = []
        visited = set()
        for i in range(numCourses):
            if i not in course_to_prereq:
                # no pre-requisite
                self.coursesLeft -= 1
                startingCourses.append(i)
        
        def helper(course: int, visited: Set[int]) -> bool:
            if course in prereq_to_course and prereq_to_course[course] not in visited:
                visited.add(prereq_to_course[course])
                if helper(prereq_to_course[course], visited):
                    self.coursesLeft -= 1

        #     for key, val in course_to_prereq.items():
        #         if course == val and key not in visited:
        #             # we can take this course (key) because we got the pre-req 
        #             visited.add(key)
        #             if helper(key, course_to_prereq, visited):
        #                 self.coursesLeft -= 1
        # print(startingCourses)
        for course in startingCourses:
            visited.add(course)
            helper(course, visited)
        
        return self.coursesLeft == 0

sol = Solution()
output = sol.canFinish(3, [[1,0],[1,2],[0,1]])
print(output)