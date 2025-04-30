class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dir = [(0 , 1) , (0 , -1) , (-1 , 1) , (1 , -1) , (1 , 0) , (-1 , 0) , (1 , 1) , (-1 , -1)]
        n , m = len(board) , len(board[0]) 
        x = click[0]
        y = click[1]
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        
        def inbound(row , col):
            return 0 <= row < n and 0 <= col < m
       
        queue = deque([(x , y)])
        while queue:     
            u , v = queue.popleft()
            if board[u][v] == "E":
                count = 0
                for rw , cl in dir:
                    row = u + rw
                    col = v + cl
                    if inbound(row , col):
                        if board[row][col] == "M":
                            count += 1

                if count == 0:
                    board[u][v] = "B"
                    for rw , cl in dir:
                        row = u + rw
                        col = v + cl
                        if inbound(row , col):
                            if board[row][col] == "E":
                                queue.append((row , col))

                else:
                    board[u][v] = str(count)
                    
        return board


