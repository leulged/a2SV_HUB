class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        max_nice_substring = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub_str = s[i:j]

                if self.isNice(sub_str) and len(sub_str) > len(max_nice_substring):
                    max_nice_substring = sub_str

        return max_nice_substring

    def isNice(self, sub: str) -> bool:
        char_set = set(sub)
        
        for c in sub:
            if c.lower() not in char_set or c.upper() not in char_set:
                return False 
        
        return True  
