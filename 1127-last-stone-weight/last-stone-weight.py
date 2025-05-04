class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for wei in stones:
            heappush(heap , -wei)
        
        while len(heap) > 1:
            x = -heappop(heap)
            y = -heappop(heap)
            
            if x == y:
                continue
            
            else:
                if x < y:
                    y = y - x
                    heappush(heap , -y)
                
                else:
                    x = x - y
                    heappush(heap , -x)
        
        if heap:
            return -heap[0]
        
        return 0