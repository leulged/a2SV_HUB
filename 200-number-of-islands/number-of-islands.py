class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(0 , 1) , (1 , 0) , (0 , -1) , (-1 , 0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def inbound(row , col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(row , col):
            visited[row][col] = True

            for x , y in direction:
                new_row = row + x
                new_col = col + y

                if inbound(new_row , new_col):
                    if grid[new_row][new_col] == '1' and not visited[new_row][new_col]:
                        dfs(new_row , new_col)

            

        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and not visited[row][col]:
                    dfs(row , col)
                    ans += 1
        
        return ans