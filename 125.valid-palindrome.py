# @leet start
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if len(s) < 2:
            return True
    
        mid = len(s) // 2

        if len(s) % 2 == 0:
            # Even 
            return s[:mid] == s[mid:][::-1]
        else:
            # Odd 
            return s[:mid] == s[mid+1:][::-1]
# @leet end
