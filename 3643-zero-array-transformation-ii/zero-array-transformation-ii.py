class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        def check(k):
            prefix = [0] * (n + 1)
            
            for i in range(k):
                left , right , val = queries[i]
                prefix[left] -= val
                prefix[right + 1] += val
            
            curr_decrement = 0
            current = nums[:]
            for i in range(n):
                curr_decrement += prefix[i] 
                current[i] += curr_decrement  
                
                if current[i] > 0:
                    return False  

            return True  

        left , right = 0 , len(queries)
        ans = -1

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            
            else:
                left = mid + 1

        return ans