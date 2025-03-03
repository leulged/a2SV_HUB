class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == "R":
                r += 1

            else:
                l += 1
            
            if l == r:
                ans += 1
                l = r = 0
                
        return ans
        