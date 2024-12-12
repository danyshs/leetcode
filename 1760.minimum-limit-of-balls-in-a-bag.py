# @leet start
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can_divide(max_bag_size: int) -> bool:
            # Calculate total operations needed if max size of a bag is `max_bag_size`
            # (x - 1) // max_bag_size gives the number of splits needed for `x`
            return sum((x - 1) // max_bag_size for x in nums) <= maxOperations

        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if can_divide(mid):
                right = mid
            else:
                left = mid + 1
        return left
       
   # @leet end
