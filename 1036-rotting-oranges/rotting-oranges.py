class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0)) 
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        directions = [(-1,0), (1,0), (0,-1), (0,1)]  
        minutes_passed = 0

        while queue:
            r, c, minute = queue.popleft()
            minutes_passed = max(minutes_passed, minute)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  
                    fresh_oranges -= 1
                    queue.append((nr, nc, minute + 1))

        return minutes_passed if fresh_oranges == 0 else -1
