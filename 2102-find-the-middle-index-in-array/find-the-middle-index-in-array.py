class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0]*(len(nums)+1)
        prefix[1] = nums[0]

        for i in range(2,len(prefix)):           
            prefix[i] = prefix[i-1] + nums[i-1]
        for i in range(1,len(prefix)):
            right=0
            if i==len(prefix)-1:
                right=0

            else:
                right = prefix[-1] - prefix[i]
            left=prefix[i-1]
            if left == right:
                return i-1
        return -1