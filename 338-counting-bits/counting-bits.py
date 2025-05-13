class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n + 1):
            count = 0
            while num > 0:
                if num & 1 != 0:
                    count += 1
                
                num = num >> 1
                
            ans.append(count)
        
        return ans