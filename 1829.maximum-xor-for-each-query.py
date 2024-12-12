# @leet start
class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        n = len(nums)
        
        prev_xor = [0]
        for num in nums:
            prev_xor.append(prev_xor[-1] ^ num)
        
        # Find the maximum possible XOR value
        max_xor = (1 << maximumBit) - 1
        
        # Compute the answers for each query
        answer = []
        for i in range(n):
            # Find the value of k that maximizes the XOR
            k = max_xor ^ prev_xor[n - i]
            answer.append(k)
            
            # Remove the last element from the array
            prev_xor.pop()
        
        return answer
# @leet end

# XOR is a reverse OR

# 0 0 | 0
# 0 1 | 1
# 1 0 | 1
# 1 1 | 1

# maximumBit = 2
# Question: [0,1,1,3]
# Answer: [0,0,0,0]
# 
# for j in range(len):
#   for range(0,len-1) in Question:
#       XOR(Question[i],Question[i+1]
# 
#   Answer[j] = Math.max(XOR(Question), maximumBit)
# 
#   Question.pop()
# Return Answer
# Helper XOR:
# Return 

