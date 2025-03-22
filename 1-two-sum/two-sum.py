class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDic={}
        for i in range(len(nums)):
            x=target-nums[i]
            if nums[i] not in myDic:
                myDic[x]=i
            else:
                return [myDic[nums[i]],i]        
        
           
        
        