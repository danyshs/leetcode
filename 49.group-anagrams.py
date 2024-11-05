from collections import defaultdict
from typing import List
# @leet start

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - 97] += 1
            hmap[tuple(count)].append(s)  
        return list(hmap.values())

# @leet end
