class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        
        ans = [[-1 for _ in range(m)] for _ in range(n)]  
        queue = deque()

        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row , col):
            return 0 <= row < n and 0 <= col < m

        for i in range(n):
            for j in range(m):
                
                if isWater[i][j] == 1:
                    ans[i][j] = 0
                    queue.append((i, j))
        
        while queue:
            row , col = queue.popleft()

            for x , y in dir:
                new_row = row + x
                new_col = col + y

                if inbound(new_row , new_col):

                    if ans[new_row][new_col] == -1:
                        ans[new_row][new_col] = ans[row][col] + 1
                        queue.append((new_row , new_col))

        return ans