class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acc=1
        prefix=[]
        for i in range(len(nums)):
            if nums[i] != 0:
                acc *= nums[i]
                prefix.append(acc)
        if 0 not in nums:            
            ans=[]
            for i in range(len(nums)):
                ans.append(prefix[-1]//nums[i])
            return ans

        else:
            count_zero=Counter(nums)
            if count_zero[0]>1:
                return [0]*len(nums)
            else:
                for i in range(len(nums)):
                    if nums[i] != 0:
                        nums[i]=0
                    else:
                        nums[i]=prefix[-1]
                return nums