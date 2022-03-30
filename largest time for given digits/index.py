'''
Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.

 

Example 1:

Input: arr = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.
Example 2:

Input: arr = [5,5,5,5]
Output: ""
Explanation: There are no valid 24-hour times as "55:55" is not valid.
 

Constraints:

arr.length == 4
0 <= arr[i] <= 9

'''
'''
brute method way is doing 4 for loops
which isnt too bad because it only runs O(1) time 24 times
highest variable which is 2359.  

'''

'''
beautify?
maybe make time property a class and update it's properties if the length of output isnt 5
we run maximum of 3 time if failing. with first index being max number of 2, 1, 0. 
make code into a function for re-calling if failed.
'''
from typing import List
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        timeProperties = {
                            (0, 2): "",
                            (1, 9): "",
                            (2, 0): ":",
                            (3, 5): "",
                            (4, 9): ""
                        }
                        # (9, 1) can become (3, 1) max num 3 if (2,0) has a number
        latestTime = ""
        # sort 
        sortedNums = sorted(arr, reverse=True) # [1,2,3,4]
        # update time properties if 1 or 2 exists
        if  2 in sortedNums:
            timeProperties = {
                            (0, 2): "",
                            (1, 3): "",
                            (2, 0): ":",
                            (3, 5): "",
                            (4, 9): ""
                        }
        for num in sortedNums:
            for property in timeProperties: # property = (#, #)
                if num <= property[1] and len(timeProperties[property]) == 0:
                    timeProperties[property] += str(num)
                    break
        

        for property in timeProperties:
            latestTime += timeProperties[property]


        if len(latestTime) < 5:
            latestTime = ""
            timeProperties = {
                            (0, 1): "",
                            (1, 9): "",
                            (2, 0): ":",
                            (3, 5): "",
                            (4, 9): ""
                        }
            for num in sortedNums:
                for property in timeProperties: # property = (#, #)
                    if num <= property[1] and len(timeProperties[property]) == 0:
                        timeProperties[property] += str(num)
                        break
            for property in timeProperties:
                latestTime += timeProperties[property]

            if len(latestTime) < 5:
                latestTime = ""
                timeProperties = {
                                (0, 0): "",
                                (1, 9): "",
                                (2, 0): ":",
                                (3, 5): "",
                                (4, 9): ""
                            }
                for num in sortedNums:
                    for property in timeProperties: # property = (#, #)
                        if num <= property[1] and len(timeProperties[property]) == 0:
                            timeProperties[property] += str(num)
                            break
                for property in timeProperties:
                    latestTime += timeProperties[property]
                if len(latestTime) < 5:
                    return ""
                return latestTime

            return latestTime
        return latestTime

sol = Solution()

output = sol.largestTimeFromDigits([1,2,3,4])
print(output)

output = sol.largestTimeFromDigits([0,5,5,5])
print(output)

output = sol.largestTimeFromDigits([2,0,6,6])
print(output)

output = sol.largestTimeFromDigits([2,9,1,8])
print(output)










