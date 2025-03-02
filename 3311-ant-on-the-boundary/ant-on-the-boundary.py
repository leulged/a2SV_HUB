class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        n  = len(nums)
        cnt =0
        pt = 0

        for i in range(n):
            pt += nums[i]
            if pt == 0 :
                cnt += 1
                                
        return cnt
            