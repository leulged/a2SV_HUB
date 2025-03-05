class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ind = set()
        count = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                ind.add(i)
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i + 1 not in ind and i - 1 not in ind:
                    count += 1
                    ind.add(i)
                
        if count >= n:
            return True
        return False