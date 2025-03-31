class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        left , right = 0 , len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2

            if minimum <= nums[mid]:
                left = mid + 1
            
            else:
                minimum = nums[mid]
                right = mid - 1
        
        return minimum