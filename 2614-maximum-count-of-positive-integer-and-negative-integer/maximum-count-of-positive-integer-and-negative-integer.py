class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        zeros = nums.count(0) 
        
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= 0: 
                if mid == 0 or nums[mid - 1] < 0:
                    return max(mid, len(nums) - mid - zeros)  

                right = mid - 1
                
            else: 
                left = mid + 1

        return len(nums) 
