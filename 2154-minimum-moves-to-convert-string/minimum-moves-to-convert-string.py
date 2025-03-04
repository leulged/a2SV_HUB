class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        cnt = 0
        flag = False
        three = 0
        for i in range(n):
            if s[i] == "X":
                three += 1
            
            if s[i] == "O" and three > 0:
                three += 1

            if three == 3:
                cnt +=1
                three = 0
            
            if three > 0 and i == n - 1:
                cnt += 1
        return cnt

        
