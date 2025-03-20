class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        form = []
        def sub(start ):
            if start == len(nums):
                ans.append(form[:])
                return 

            
            form.append(nums[start])
            sub(start + 1)
            form.pop()
            sub(start + 1)
                
        sub(0)
        return ans

            