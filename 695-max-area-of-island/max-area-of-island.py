class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [(1 , 0) , (-1 , 0) ,(0 , 1) ,(0 , -1)]
        n , m = len(grid) , len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        def in_bound(row , col):
            return 0 <= row < n and 0 <= col < m
        mx = 0
        def dfs(row , col):
            
            visited[row][col] = True
            area = 1
            
            for x , y in dir:
                new_row = row + x
                new_col = col + y
                if in_bound(new_row , new_col):
                    if grid[new_row][new_col] == 1 and not visited[new_row][new_col]:
                        
                        area += dfs(new_row , new_col )
                        
            return area
            

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    
                    result = dfs(row , col)
                    mx = max(result , mx)

        return mx