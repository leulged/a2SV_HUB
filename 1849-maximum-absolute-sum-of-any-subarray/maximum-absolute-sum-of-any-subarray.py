class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]
        mx=[nums[0]]
        mn=[nums[0]]
        #try to get the maximum negative or maximum positive subarray sum
        for i in range(1, len(nums)):         
            max_sum = max(nums[i] , nums[i] + max_sum)
            mx.append(abs(max_sum))

            min_sum = min(nums[i] , nums[i] + min_sum)
            mn.append(abs(min_sum))

        #try to get the maximum  absolute value
        curr_min = abs(max(mn))
        curr_max = abs(max(mx))

        return max(curr_min , curr_max)

        