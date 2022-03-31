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
brute force using DFS
[0,1,0,3,2,3]
meaning we want to generate every possible subsequeence we have a choice fo reach value right so for the first 0
we have a choice: are we going to include this 0 in our subsequence or are we not going to include it in our subsequence
so in reality for each value we have two choices now when we get to the next value we also have a choice are we going to include it or not
as you see, the time complexity O(2^n) is not great. can we modify it to get a better solution like O(n^2). let's look at another example this time
we're going to do DFS with caching.
let's start off with a brute force approach. let's check all subseqeuences starting at index 0 and then repeat that starting index at one, then at index two, then at index three and so on.
[1,2,4,3]
let's focus on this caching part. what kind of repeated work have we eliminated. well let's do this out of order instead of doing these first
let me show you what happens if we try to extend the three now.
LIS starting at index 3, we cannot increase it anymore since we are at the last index. we do not need to repeat this work.
going back to the first example of [1,2,3] as soon as we get to the 3 we know we could not increase this subsequence anymore. we are only able to add 1 element if we start at index 3.
[1,2,4]
that's exactly what this index 2 tells us too. if we start at index 2, we can only add a 4 and we cannot include anything after that.
we knew the longest increasing subsequence starting at index 2 is also 1.
what about index 1? we would start with the subsequence of 2. we saw both of them already [1,2,4] [1,2,3]
longest starting at index 1 is going to be length 2 either way. if we start at 2, we can add either 4 or a 3. longest increasing subsequence starting at index 1 is going to be length 2. so we don't even need to go down this path once we already go down here because it's going to be repeated work.
we when we finally in our DFS get back to the root we're gonna see that the longest path is one of these right [1,2,4], [1,2,3]. the longest length starting at index 0 is going to be 3.
if you want to do the dynammic programming solution, you might notice how we're doing this recursively we're kind of starting at the last index three and working our way up backwards to zero. so then going back here we use that to do dynammic programming.
so we're going to start at the last index 3 and then work our way backward so we know this is kind of the base case right. no values comes after index 3. so the LIS[3] = 1. How do we get the LIS starting at index 2? one possiblitiy is 4 by itself. it could be 1, or it could be 1 + LIS[3]. we are only allowed to do this if nums[2] < nums[3]. is this true? this is not true. so we are not allowed to do this. LIS[2] = 1.
so again we work ourself backwards. LIS[1] = max(1, 1 + LIS[2], LIS[3]). we are allowed to do this because it is increasing. we know both are 2 so LIS[1] = 2 regardless.
 so we want LIS[0] = max(1,1+2(1 + LIS[1]), 1+1 (1+LIS[2]), 1+1 (1+LIS[3]) )
 we are allowed to do all of this because all of them in increasing order. so LIS[0] = 3. the dynammic programming is much better because time complexity O(n^2). But why is it O(N^2)? well you see we're working backwards we start at index 3 then check every position afterwards whicfh is not too bad right so then we iterate throguh basically every value here. when we start at index 2, we have to look at every value after it, which is index 3. If we start at index 1, we look at every value after it which is index 2, index 3. and so on with index 0. this pattern is similar to an n squared pattern.

 we know we are doing this dynammic programming stlye so lets have a cache or a list initally going to be set to 1 for every value and it's going to be the length of the input array we are given
 so every longest increasing subsequence starting at every value or every index is initially just set to one. we're going to try to find what the max is so we want to interate through every index in the range of our input array and we want to do it in reverse order. i'm starting at the last index and then going all the way to zero.

just like in the example we're going to start at index i which is the last index and iterate through every subsequence that came after it so im going to have another nested loop for j in range so starting at i+1 and going to the end of the input array.

before we can update LIS, we want to know is the value at i actually less than the value at j becfause j comes after it if we want this to be an increasing subsequence this condition has to be true and only then are we allowed to update the longest increasing subsequence. then we can set it to the max of itself or the max of 1 + LIS[j] starting at j because we know for sure j is going to be in increasing order with i.

and literally that is it. we make sure to evaluate that it's an increasing order we did it backwards we made sure to cache the repeated work. what we have left to do is to return what the max is. In python you can just take the max of the list.

This is O(n^2). there actually is a better solution o(nlogn) but not going to cover here.
'''



from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums), -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        # print('LIS', LIS)
        return max(LIS)
             

solution = Solution()


# output = solution.lengthOfLIS([10,3,9,2,5,3,7,101,18])
# print(output)

# output = solution.lengthOfLIS([0,1,0,3,2,3])
# print(output)

# output = solution.lengthOfLIS([0,1,2,4])
# print(output)

# output = solution.lengthOfLIS([-813,82,-728,-82,-432,887,-551,324,-315,306,-164,-499,-873,-613,932,177,61,52,1000,-710,372,-306,-584,-332,-500,407,399,-648,290,-866,222,562,993,-338,-590,303,-16,-134,226,-648,909,582,177,899,-343,55,629,248,333,1,-921,143,629,981,-435,681,844,349,613,457,797,695,485,15,710,-450,-775,961,-445,-905,466,942,995,-289,-397,434,-14,34,-903,314,862,-441,507,-966,525,624,-706,39,152,536,874,-364,747,-35,446,-608,-554,-411,987,-354,-700,-34,395,-977,544,-330,596,335,-612,28,586,228,-664,-841,-999,-100,-620,718,489,346,450,772,941,952,-560,58,999,-879,396,-101,897,-1000,-566,-296,-555,938,941,475,-260,-52,193,379,866,226,-611,-177,507,910,-594,-856,156,71,-946,-660,-716,-295,-927,148,620,201,706,570,-659,174,637,-293,736,-735,377,-687,-962,768,430,576,160,577,-329,175,51,699,-113,950,-364,383,5,748,-250,-644,-576,-227,603,832,-483,-237,235,893,-336,452,-526,372,-418,356,325,-180,134,-698])
# print(output)
