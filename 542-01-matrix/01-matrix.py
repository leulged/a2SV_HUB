class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dir = [(1 , 0) , (-1 , 0) , (0 , 1) , (0 , -1)]
        n = len(mat)
        m = len(mat[0])
        ans = [[0 for _ in range(m)] for _ in range(n)]
        visit = [[0 for _ in range(m)] for _ in range(n)]
        def inbound(row , col):
            return 0 <= row < n and 0 <= col < m

        queue = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i , j))
        
        while queue:
            row , col = queue.popleft()

            for x , y in dir:
                new_row = row + x
                new_col = col + y

                if inbound(new_row , new_col):
                   if mat[new_row][new_col] == 1:
                        mat[new_row][new_col] = 0  
                        ans[new_row][new_col] = ans[row][col] + 1
                        queue.append((new_row, new_col))


        return ans

