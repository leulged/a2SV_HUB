class Solution:
    def rob(self, nums: List[int]) -> int:
        memory = {}
        def dp(i):
            if i == len(nums) - 2 or i == len(nums) - 1:
                return nums[i]

            if i in memory:
                return memory[i]

            if i + 3 == len(nums):
                memory[i] = nums[i] + dp(i + 2)
            else:
                memory[i] = nums[i] + max(dp(i + 2) , dp(i + 3))

            return memory[i]

        if len(nums) == 1:
            return nums[0]

        return max(dp(0) , dp(1))
            