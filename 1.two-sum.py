# @leet start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevmap = {}

        for i,n in enumerate(nums):
            complement = target - n
            if complement in prevmap:
                return [prevmap[complement],i]
            prevmap[n] = i
# @leet end
