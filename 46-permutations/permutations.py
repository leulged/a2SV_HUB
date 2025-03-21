class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        form = []
        def perm(start):
            if start == len(nums):
                ans.append(nums[:])
                return 
            
            for i in range(start , len(nums)):
                nums[start] , nums[i] = nums[i] , nums[start]
                perm(start + 1)
                nums[start] , nums[i] = nums[i] , nums[start]

        perm(0)

        return ans
