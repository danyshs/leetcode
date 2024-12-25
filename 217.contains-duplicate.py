# @leet start
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        box = set()
        for i in nums:
            if i in box:
                return True 
            box.add(i)
        return False 

# @leet end
