# @leet start
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        parsed_edges = [0]*n
        champions = []

        for src, dst in edges:
            parsed_edges[dst] +=1

        for i,nonzero in enumerate(parsed_edges):
            if not nonzero:
                champions.append(i)

        if len(champions) >1:
            return -1
        
        return champions[0]

# @leet end
