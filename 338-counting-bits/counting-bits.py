class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n + 1):
            count = 0
            for i in range(32):
                if num & (1 << i) != 0:
                    count += 1
                
            ans.append(count)
        
        return ans