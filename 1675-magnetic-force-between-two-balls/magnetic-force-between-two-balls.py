class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(mid):
            count = 1
            first_pos = position[0]
            for i in range(1 , len(position)):
                if position[i] - first_pos >= mid:
                    count += 1
                    first_pos = position[i]
            
            return count >= m
                

        position.sort()
        left , right = 0 , position[-1] - position[0]
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2

            if check(mid):
                ans = mid 
                left = mid + 1

            else:
                right = mid - 1
        
        return ans

