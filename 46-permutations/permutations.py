class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for perm in permutations(nums, len(nums)):
            ans.append(perm)
        
        return ans
