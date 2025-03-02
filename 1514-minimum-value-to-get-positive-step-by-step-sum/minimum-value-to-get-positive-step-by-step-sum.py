class Solution:
    def minStartValue(self, nums: List[int]) -> int:
 
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]
        
        prefix.sort()

        return 1 - prefix[0] if prefix[0] <= 0 else 1