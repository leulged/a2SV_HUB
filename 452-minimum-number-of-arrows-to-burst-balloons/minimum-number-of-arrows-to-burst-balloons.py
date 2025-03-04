class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev = points[0][1]
        count = 0
        
        if len(points) == 1:
            return 1

        for i in range(1 , len(points)):
            if prev < points[i][0]:
                count += 1
                prev = points[i][1]
            
            elif prev >= points[i][0]:
                prev = min(prev, points[i][1])

            if i == len(points) - 1:
                count += 1

        return count 

        