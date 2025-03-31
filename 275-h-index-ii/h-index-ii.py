class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left , right = 0 , len(citations) - 1
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            print(mid)
            if citations[mid] >= len(citations) - mid:
                ans = len(citations) - mid
                right = mid - 1
                
            else:
                
                left = mid + 1 
        return ans