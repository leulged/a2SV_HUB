class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 0
        od = 1
        if n == 1:
            return 1
        for _ in range(n - 1):
            ans += od * 2
            od += 2

        return ans + od