class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            ans = 1
            for i in range(1, n + 1):
                ans *= i
            
            return ans

        ans =factorial(n)
        count = 0
        
        while ans % 10 == 0:
            count += 1
            ans //= 10
        
        return count
        
        
        