class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        
        ans = 0
        flag = True
        for val in cnt.values():
            if val % 2 == 0:
                ans += val

            else:
                if flag :
                    ans += val
                    flag = False
                    
                else:
                    ans += val - 1

        return ans 

        