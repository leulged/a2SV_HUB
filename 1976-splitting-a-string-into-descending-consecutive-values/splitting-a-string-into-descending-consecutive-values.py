class Solution:
    def splitString(self, s: str) -> bool:
        curr_str = []
        
        def backtrack(start):
            if start == len(s):
                if len(curr_str) < 2:
                    return False
                for i in range(1, len(curr_str)):
                    if curr_str[i - 1] - curr_str[i] != 1:
                        return False
                return True
            
            num = 0
            for i in range(start, len(s)):
                num = num * 10 + (ord(s[i]) - ord('0'))  
                curr_str.append(num)
                
                if backtrack(i + 1):
                    return True
                
                curr_str.pop()
            
            return False
        
        return backtrack(0)
