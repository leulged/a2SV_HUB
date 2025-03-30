class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left , right = max(weights) , sum(weights)
        min_capacity = left
        
        while left <= right:
            mid = left + (right - left) // 2

            count_days = 1
            curr_capacity = 0

            for weight in weights:
                curr_capacity += weight

                if mid < curr_capacity:
                    count_days += 1
                    curr_capacity = weight
                
            if count_days <= days:
                right = mid - 1
                min_capacity = mid
            
            else:
                left = mid + 1
            
        return min_capacity