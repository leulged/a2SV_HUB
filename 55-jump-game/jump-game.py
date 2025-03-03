class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        mx = 0
        for i in range(n):
            if nums[i] != 0:
                mx = max(mx - 1 , nums[i])

            else:

                if mx + i - 1 <= i:
                    return False

                mx -= 1
                
        return True
        
       


        