# @leet start
from collections import Counter
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        return sorted(count, key = lambda x: (-count[x], x))[:k]
# @leet end

