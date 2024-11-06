# @leet start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [1] * n

        # Left 
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]

        # Right
        right = 1
        for i in range(n-1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output
# @leet end
