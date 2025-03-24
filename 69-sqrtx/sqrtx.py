class Solution:
    def mySqrt(self, x: int) -> int:
        best = 0
        left , right = 0 , x

        while left <= right:
            mid = left + (right - left) // 2
            
            if mid * mid > x:
                right = mid - 1
            
            elif mid * mid <= x:
                best = mid
                left = mid + 1

        return best