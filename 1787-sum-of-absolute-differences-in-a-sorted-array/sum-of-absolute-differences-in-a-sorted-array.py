class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        
        totalSum = prefixSum[n]  
        result = [0] * n
        
        for i in range(n):
            leftSum = i * nums[i] - prefixSum[i]  
            rightSum = (totalSum - prefixSum[i + 1]) - (n - i - 1) * nums[i]  
            result[i] = leftSum + rightSum
        
        return result
