class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mn  = float("inf")
        curr = mn

        for i in range(len(nums) - l + 1):
            for j in range(i + l, r + i + 1):
                sm = sum(nums[i:j])

                if sm>0:
                    mn = min(mn, sm)

        if mn!=curr:
            return mn
        else:
            return -1 







        
        