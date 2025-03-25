class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = 1 , max(piles)

        best = -1

        while left <= right:
            mid = (left + right) // 2

            calculated_h = 0
            for i in range(len(piles)):
                calculated_h += ceil(piles[i] / mid)
  
            if calculated_h <= h:
                right = mid - 1
                best = mid
            
            elif calculated_h > h:
                left = mid + 1
            
        return best
