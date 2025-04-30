class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        for i in range(len(heights) - 1):
            curr = heights[i + 1] - heights[i]
            if curr > 0:
                heappush(heap , curr)

                if len(heap) > ladders:
                    smallest = heappop(heap)
                    bricks -= smallest
                
                if bricks < 0:
                    return i
                
        return len(heights) - 1
        
