class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left , right = 0 , len(matrix) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] > target:
                right = mid - 1
            
            elif matrix[mid][-1] < target:
                left = mid + 1
            
            else:
                curr = matrix[mid]
                l , r = 0 , len(curr) - 1

                while l <= r:
                    
                    md = l + (r - l) // 2
                    
                    if curr[md] > target:
                        r = md - 1

                    elif curr[md]  < target:
                        l = md + 1
                    
                    else:
                        return True

                break
            

        return False

