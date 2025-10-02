class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False
        
        target_sum = total_sum // 2

        memory = {}
        def canFindSubset(index , current_sum):
            if current_sum == 0:
                return True
            
            if index >= len(nums) or current_sum < 0:
                return False
            
            if (index, current_sum) in memory:
                return memory[(index, current_sum)]

            include = canFindSubset(index + 1 , current_sum - nums[index])
            if include:
                memory[(index , current_sum)] = True
                return True
            
            exclude = canFindSubset(index + 1 , current_sum)
            memory[(index , current_sum)] = exclude

        
            return memory[(index , current_sum)]

        return canFindSubset(0 , target_sum)
        
        