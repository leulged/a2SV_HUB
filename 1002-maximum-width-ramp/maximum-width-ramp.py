class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_ = [0] * len(nums)
        curr = nums[-1]
        for i in range(len(nums) - 1 , - 1, -1):
            max_[i] = max(curr , nums[i])
            curr = max(curr , nums[i])
        max_in = 0
        l ,r = 0 , 1
        while r < len(nums):
            while r < len(nums) and nums[l] <= max_[r]   :
                r += 1
            
            
            l += 1
            max_in = max(max_in , r - l )
                
                # print(l , r)
        print(max_)
        return max_in 
            
