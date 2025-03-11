class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        curr = 0
        x = 0
        while n > curr:
            curr = 4 ** x
            if curr == n:
                return True

            x += 1
        
        return False
