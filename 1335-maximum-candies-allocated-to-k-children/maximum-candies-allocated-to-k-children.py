class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        left , right =  1 , max(candies)
        max_can = 0

        while left <= right:
            mid = left + (right - left) // 2

            count = 0
            for candy in candies:
                count += (candy // mid)
            
            if count >= k:
                max_can = mid
                left = mid + 1
            
            else:
                right = mid - 1
        
        return max_can
             