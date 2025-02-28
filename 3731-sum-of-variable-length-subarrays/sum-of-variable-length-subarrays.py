class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        print(prefix)
        ans = 0
        for i in range(n):
            st = max(0, i - nums[i])
            ans += prefix[i + 1] - prefix[st]
        
        return ans 
        