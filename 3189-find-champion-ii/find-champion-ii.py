class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        losers = [False for _ in range(n)]

        for u , v in edges:
            losers[v] = True
            
        ans = -1
        for i in range(n):
            if not losers[i]:
                if ans != -1:
                    return -1

                ans = i
        
        return ans