class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.prefix=[[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                self.prefix[i][j]=matrix[i][j]
                if i>0:
                    self.prefix[i][j] += self.prefix[i-1][j]
                if j>0:
                    self.prefix[i][j] += self.prefix[i][j-1]
                if i>0 and j>0:
                    self.prefix[i][j] -= self.prefix[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2][col2]
        
        if row1>0:
            total -= self.prefix[row1-1][col2]
        if col1>0:
            total -= self.prefix[row2][col1-1]
        if row1>0 and col1>0:
            total += self.prefix[row1-1][col1-1]

        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)