class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pos = nums.index(k)
        rep_count = defaultdict(int)
        bal = 0
        for i in range(pos, len(nums)):
            bal += 1 if nums[i] > k else (-1 if nums[i]<k else 0)
            rep_count[bal] += 1

        bal = 0
        ans = 0
        for i in range(pos , -1 ,- 1):
            bal += int(nums[i] > k) - int(nums[i] < k)
            
            ans += rep_count[-bal]
            ans += rep_count[-bal + 1]
        
        return ans