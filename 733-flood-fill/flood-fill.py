class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dir = [(0 , 1) , (1 , 0) , (0 , -1) , (-1 , 0)]
        val = image[sr][sc]
        n = len(image)
        m = len(image[0])

        if val == color:
            return image

        def inbound (row , col):
            return 0 <= row < n and 0 <= col < m
            
        visited = [[False for _ in range(m)] for _ in range(n)]

        def dfs(row , col):
            visited[row][col] = True
            image[row][col] = color

            for x , y in dir:
                new_row = x + row
                new_col = y + col
                if inbound(new_row , new_col) and not visited[new_row][new_col] and image[new_row][new_col] == val:
                    dfs(new_row , new_col)
            
            
        dfs(sr , sc)
        return image