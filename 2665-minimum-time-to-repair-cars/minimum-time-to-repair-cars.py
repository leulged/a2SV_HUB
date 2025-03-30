class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair(ranks , time):
            total_car = 0

            for rank in ranks:
                total_car += int(math.sqrt(time / rank))
            
            return total_car
        
        left , right = 1 , max(ranks) * cars ** 2
        min_time = left

        while left <= right:
            mid = left + (right - left) // 2

            total_car = can_repair(ranks , mid)

            if total_car >= cars:
                right = mid - 1
                min_time = mid
            
            else:
                left = mid + 1

        return min_time
            

        