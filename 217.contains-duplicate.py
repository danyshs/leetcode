# @leet start
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        box = set()
        for num in nums: 
            if num in box:
                return True 
            box.add(num)
        return False
            
            

# @leet end

