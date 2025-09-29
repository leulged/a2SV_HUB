class Solution:
    def rob(self, nums: List[int]) -> int:
        memory = {}
        def dp(i):
            if i >= len(nums):
                return 0

            if i in memory:
                return memory[i]
            
            memory[i] = nums[i] + max(dp(i + 2) , dp(i + 3))

            return memory[i]

        return max(dp(0) , dp(1))
            