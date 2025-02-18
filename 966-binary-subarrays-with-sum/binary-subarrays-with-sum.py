class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res=0
        sm=0
        thisdict={0:1}
        for n in nums:
            sm+=n
            if sm-goal in thisdict:
                res+=thisdict[sm-goal]
            if sm not in thisdict:
                thisdict[sm]=1  
            elif sm  in thisdict:
                thisdict[sm]+=1              
            
        return res