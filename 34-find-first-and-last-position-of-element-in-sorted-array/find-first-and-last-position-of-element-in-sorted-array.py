class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans =[-1 , -1]
        low , high = 0 , len(nums) - 1
        while low <= high:
            mid = low + (high - low) //2

            if nums[mid] == target:
                ans[0] = mid
            
            if nums[mid] >= target:
                high = mid - 1
            
            elif nums[mid] < target:
                low = mid + 1
        
        low  , high = 0 , len(nums) - 1

        while low  <= high:
            mid = (low + high) //2
            if nums[mid] == target:
                ans[1] = mid
            
            if nums[mid] > target:
                high = mid - 1
            
            elif nums[mid] <= target:
                low = mid + 1

        return ans
