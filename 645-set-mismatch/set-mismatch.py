class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []

        while i < len(nums):
            if nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1] , nums[i] = nums[i] , nums[nums[i] - 1]
            
            else:
                i += 1
        
        for i in range(len(nums)):
            if i != nums[i] - 1:
                ans.append(nums[i])
                ans.append(i + 1)
                
        
        return ans