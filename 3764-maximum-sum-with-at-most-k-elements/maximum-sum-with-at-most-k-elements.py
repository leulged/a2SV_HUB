class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []

        for i , val in enumerate(grid):
            for gr in val:
                heappush(heap , (-gr , i))
        
        ans = 0

        while k > 0:
            val , ind = heappop(heap)
            if limits[ind] > 0:
                ans += -val
                limits[ind] -= 1
                k -= 1
                
        return ans

            