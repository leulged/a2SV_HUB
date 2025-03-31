class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def check(radius):
            j = 0
            for house in houses:
                while j < len(heaters) - 1 and abs(heaters[j + 1] - house) <= abs(heaters[j] - house):
                    j += 1

                x = abs(house - heaters[j])
                if x > radius:
                    return False
                
            return True
        
        heaters.sort()
        houses.sort()
        left , right = 0 , max(houses[-1] ,heaters[-1])  - min(houses[0], heaters[0])
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2

            if check(mid):
                ans = mid
                right = mid - 1
            
            else:
                left = mid + 1
        
        return ans


