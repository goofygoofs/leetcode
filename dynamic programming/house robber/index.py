'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them 
is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

[2,1,1,2,1,1,2,100] => 2, 2, 1, 100 = > 105
output: 4
skips 2...


stack => [(2, idx), idx+1 value, pop last one and add current]

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
'''
'''

story:
we're basically given an array of integers and each integer represents a house and how much we can rob from that house
we want to rob houses to maximize the amount of money we can rob. 
there is a restriction, we can't rob two houses that are adjacent to each other
let's start out with the brute force approach.
imagine we try to get every single combination.
the first combination is where we pick the first house so let's draw out what the decision tree would look like
we cant rob the next one so we have to basically get the max we can rob from these two so it kind of sounds like a sub problem
continuing with just a brute force, we want to rob these two houses right.
we can't rob both of them because they're right next to each other
so we can rob house 3 or we can rob house 1 so this is the decision tree.
so; we can rob house 1 and 3 or we can rob house 1 and 1 obviously we choose 1 and 3
the maximum gives us 4
but what is we didnt rob the first house we decide to rob the second so that would be our other decision in our decision tree right
if we went along this pathway in our decision tree, we would get these two houses robbed and that's a total of 3 but we remember we found this which was a total of four
that is a very brute force approach imagine if we have more numbers here it could get very complex
how can we improve it can we identify any subproblem and the answer to that is yes
let's take a look at the subproblem so remember we have two choices
we want to get the max that we can rob from this entire neighborhood so the first choice
is we rob from the first house and then fin dthe maximum from the remaining houses
there could be a three or four whatever right this is the subproblem
we're finding the max of a sub array of the entire array
second choice we have is we skip this house and we skip it then basically we're saying okay
find the maximum of the entire sub array not incluiding the first value, so let's actually write out the relationship
ROB in this case represent the maximum we can rob from the entire array
1st decsion is we're gonna rob the first value so array of index 0
plus rob the remainder of this rest portion from index 2 to the end (n).
that's our first decision to rob the first house then we're gonna break the problem into a sub problem
now we got to rob the remainder of that array skipping one of the values
if we didnt rob the first house and then we simply only have the sub-problem robbed every house skipping the first house
start at house 1 not house 0 and go until the end of the array. so thnis is the recurrence relationship. basically a way to break up dynamic programming problems. 
notice the result of the entire problem depends on only these two. if we can compute these two then we have our result
but notice each rob can be broken up into its own sub-problem just like we did over here. so let's actually sovle the subproblems now

# since we only need to maintain the last two maxes we could rob from we only need two variables
because if we get an empty sub-array we want to return zero anyway
rob1, rob2 = 0, 0

#so let's iterate through each of the houses we can rob and now we want to compute the maximum
that we can rob up and tell this value n so i'm gonna compute that in a temporary variable for now
and you'll probably see why so the max we can rob up until now in my case
im gonna say rob 1 or rob 2 was the last house that we robbed
rob 1 was the one before that.
knowing that the max we can get would be n + rob 1 meaning there was a gap
between the current house and the previous house or rob 2 which includes the previous house
if case this isnt clear let me make a comment to show what I mean by rob 1 and rob 2
rob 1 is first
rob 2 comes second and then we get msome more values and n plus 1 and so on
if i want to rob n i have to rob rob1 as well to get the maximum. i cant use rob 2
so we we iterate to the next position we wanna update rob 1 to equal rob 2
and rob2 in this case wants to equal n
we want to return rob 2 because by the time we get to the end rob 2 will be equal to the last value meaning
it will be the max we can rob from

for num in nums:
    temp = max(num + rob1, rob2)
    rob1 = rob2
    rob2 = temp


time complexity O(n)
space O(1)
'''
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        prevPrevRobbed, prevRobbed = 0, 0  #[rob1, rob2, n, n+1, ...]

        for currRobbed in nums: #[2,1,1,100]
            highestRobbedSoFar = max(currRobbed + prevPrevRobbed, prevRobbed) #(2+0,0)... (1+0,2)... (1+2, 2)
            prevPrevRobbed = prevRobbed # 0...2...2
            prevRobbed = highestRobbedSoFar # 2...2...3
        return currRobbed
    




solution = Solution()
output = solution.rob([1,2,3,1])
print(output)

output = solution.rob([2,7,9,3,1])
print(output)

output = solution.rob([2,1,1,2])
print(output)

output = solution.rob([2,1,1,2,1,1,2,100])
print(output)
