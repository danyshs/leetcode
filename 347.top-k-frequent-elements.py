# @leet start
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        return sorted(count, key = lambda x: (-count[x],x))[:k]
# @leet end
