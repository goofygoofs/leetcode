'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,3,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
'''

'''
store the current smallest number
smallest = 2
{
    10: [10]
    9: [9]
    3: [3, 4, 5, 6,7]
    2: [0,7]
    1: [1,2]
    2: [2]
}
brute force method On^2

{
    startingNum: {lastNum: length}
}


'''
from typing import List, Set
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seen = set()
        if len(nums) == 0:
            return 0
        maxLength = 0
        for i, num in enumerate(nums): #  [0,1,0,3,2,3] [0,1,2,3]
            # print('i', i, 'num', num)
            maxLength = max(maxLength, self.lengthOfLISRecursive(nums[i:], [nums[i]], seen))
        return maxLength

    def lengthOfLISRecursive(self, nums: List[int], sequence: List[int], seen: Set[int]) -> int:
        # print('SEQUENCE', sequence, 'seen', seen)
        
        maxSequence = len(sequence)

        # print('1', seen)
        for i in range (1, len(nums)):
            if nums[i] > sequence[-1]:
                
                localSequence = sequence.copy()
                localSequence.append(nums[i])
                if tuple(localSequence) not in seen:
                    seen.add(tuple(localSequence))
                else:
                    return maxSequence
                # print('LOCAL', localSequence )
                if nums[i] == sequence[-1] + 1:
                    # print('Z', i)
                    sequence.append(nums[i])
                    maxSequence = max(maxSequence, len(sequence))
                else:
                    # print('i', i, 'nums[i]', nums[i], 'sequence', sequence)
                    # seen.add(tuple(localSequence))
                    # print(seen)
                    
                    maxSequence = max(maxSequence, self.lengthOfLISRecursive(nums[i:], localSequence, seen))
              
                # print('MAX IS', maxSequence)
        return maxSequence
solution = Solution()


# output = solution.lengthOfLIS([10,3,9,2,5,3,7,101,18])
# print(output)

# output = solution.lengthOfLIS([0,1,0,3,2,3])
# print(output)

# output = solution.lengthOfLIS([0,1,2,4])
# print(output)

# dumb = [-813,82,-728,-82,-432,887,-551,324,-315,306,-164,-499,-873,-613,932,177,61,52,1000,-710,372,-306,-584,-332,-500,407,399,-648,290,-866,222,562,993,-338,-590,303,-16,-134,226,-648,909,582,177,899,-343,55,629,248,333,1,-921,143,629,981,-435,681,844,349,613,457,797,695,485,15,710,-450,-775,961,-445,-905,466,942,995,-289,-397,434,-14,34,-903,314,862,-441,507,-966,525,624,-706,39,152,536,874,-364,747,-35,446,-608,-554,-411,987,-354,-700,-34,395,-977,544,-330,596,335,-612,28,586,228,-664,-841,-999,-100,-620,718,489,346,450,772,941,952,-560,58,999,-879,396,-101,897,-1000,-566,-296,-555,938,941,475,-260,-52,193,379,866,226,-611,-177,507,910,-594,-856,156,71,-946,-660,-716,-295,-927,148,620,201,706,570,-659,174,637,-293,736,-735,377,-687,-962,768,430,576,160,577,-329,175,51,699,-113,950,-364,383,5,748,-250,-644,-576,-227,603,832,-483,-237,235,893,-336,452,-526,372,-418,356,325,-180,134,-698]
# for i in range(len(dumb)):
#     output = solution.lengthOfLIS(dumb[:i])
#     print(output)


# output = solution.lengthOfLIS([-813,82,-728,-82,-432,887,-551,324,-315,306,-164,-499,-873,-613,932,177,61,52,1000,-710,372,-306,-584,-332,-500,407,399,-648,290,-866,222,562,993,-338,-590,303,-16,-134,226,-648,909,582,177,899,-343,55,629,248,333,1,-921,143,629,981,-435,681,844,349,613,457,797,695,485,15,710,-450,-775,961,-445,-905,466,942,995,-289,-397,434,-14,34,-903,314,862,-441,507,-966,525,624,-706,39,152,536,874,-364,747,-35,446,-608,-554,-411,987,-354,-700,-34,395,-977,544,-330,596,335,-612,28,586,228,-664,-841,-999,-100,-620,718,489,346,450,772,941,952,-560,58,999,-879,396,-101,897,-1000,-566,-296,-555,938,941,475,-260,-52,193,379,866,226,-611,-177,507,910,-594,-856,156,71,-946,-660,-716,-295,-927,148,620,201,706,570,-659,174,637,-293,736,-735,377,-687,-962,768,430,576,160,577,-329,175,51,699,-113,950,-364,383,5,748,-250,-644,-576,-227,603,832,-483,-237,235,893,-336,452,-526,372,-418,356,325,-180,134,-698])
# print(output)
