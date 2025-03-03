class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = Counter(s) 
        one = cnt["1"]
        zero = cnt["0"]
        ans = ""
  
        for i in range(one - 1):
            ans += "1"

        for i in range(zero):
            ans += "0"
        
        return ans + "1"
        
        