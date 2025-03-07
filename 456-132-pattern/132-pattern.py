class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] 
        min_k = float('-inf')  
        for i in range(len(nums) - 1, -1, -1):  
            if nums[i] < min_k: 
                return True

            while stack and stack[-1] < nums[i]:  
                min_k = stack.pop()  

            stack.append(nums[i])  

        return False
