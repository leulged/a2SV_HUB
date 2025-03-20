class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        form = []
        def sub(start):
            if start > len(nums):
                return 

            ans.append(form[:])

            for i in range(start , len(nums)):
                form.append(nums[i])
                sub(i + 1)
                form.pop()
        sub(0)
        return ans


            