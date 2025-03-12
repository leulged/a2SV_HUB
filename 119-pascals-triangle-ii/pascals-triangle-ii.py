class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(n):
            ls = [1]

            for i in range(1, len(n)):        
                ls.append(n[i - 1] + n[i])
            ls.append(1)  

            return ls
        
        if rowIndex == 0:
            return [1]
        
        return pascal(self.getRow(rowIndex - 1))