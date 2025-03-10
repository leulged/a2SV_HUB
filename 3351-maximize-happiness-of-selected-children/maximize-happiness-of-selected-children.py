class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        ans = 0
        count = 0
        r = len(happiness) - 1
        
        for i in range(k):

            if happiness[r] - count > 0:
        
                ans += happiness[r] - count
                count += 1
                r -= 1
                
        return ans
