class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0] * len(nums)

        for start , end in requests:
            prefix[start] += 1

            if end<len(nums)-1:
                prefix[end+1] -= 1

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]

        prefix.sort()
        nums.sort()
        ans = 0

        for i in range(len(nums)):
            ans += nums[i] * prefix[i]
        
        return ans % (10**9 + 7)