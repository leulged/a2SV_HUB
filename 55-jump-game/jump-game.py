class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        mx = 0
        for i in range(n):

            if mx + i - 1 <= i and nums[i] == 0:
                return False

            mx = max(mx - 1 , nums[i])
        return True
        
       


        