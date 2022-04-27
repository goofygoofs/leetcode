'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

'''
for loop with pop and appending that pop back into nums , will keep consistent length
and returning result into perms which we can add the popped result into . we add into result and the first layer permute will reutrn the
correct len for result.
'''

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # base case
        if len(nums) == 1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            # print('i', i, 'nums', nums)
            n = nums.pop(0)
            perms = self.permute(nums)
            # print('perms', perms)

            for perm in perms:
                perm.append(n)
            # print('PERM', perm)
            res.extend(perms)
            # print('res', res)
            nums.append(n) # was only 3, because 2 popped off, now [3,2]
            # print('nums', nums)
        return res

# sol = Solution()
# output = sol.permute([1,2,3])
# print(output)