class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        my_dic = {}
        for i in range( len(nums2)):

            if res:
                
                while res and nums2[i] > res[-1]:
                    x = res.pop()
                    my_dic[x] = nums2[i]
                    
                    
                res.append( nums2[i])
                
            else:
                    res.append(nums2[i])
        ans = []
    
        for num in nums1:
            if num in res:
                ans.append(-1)
            
            else:
                ans.append(my_dic[num])
              
        return ans