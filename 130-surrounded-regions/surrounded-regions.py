class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visit = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        def dfs(row, col):
            visit[row][col] = True
            for x, y in dir:
                new_row = row + x
                new_col = col + y
                if inbound(new_row, new_col):
                    if  not visit[new_row][new_col] and board[new_row][new_col] == 'O':
                        dfs(new_row, new_col)

        for row in range(len(board)):
            for col in [0, len(board[0])-1]:  
                if board[row][col] == 'O' and not visit[row][col]:
                    dfs(row, col)

        for col in range(len(board[0])):
            for row in [0, len(board)-1]:  # check the first and last row
                if board[row][col] == 'O' and not visit[row][col]:
                    dfs(row, col)

        # After DFS, convert the remaining 'O's to 'X'
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O' and not visit[row][col]:
                    board[row][col] = 'X'
