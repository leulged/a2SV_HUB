class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(row, col):
            nonlocal ans
            visited[row][col] = True
            ans += 4
            for dr, dc in direction:
                new_row, new_col = row + dr, col + dc
                if inbound(new_row, new_col):
                    if grid[new_row][new_col] == 1:
                        ans -= 1 
                    if grid[new_row][new_col] == 1 and not visited[new_row][new_col]:
                        dfs(new_row, new_col)

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return ans  

        return 0
