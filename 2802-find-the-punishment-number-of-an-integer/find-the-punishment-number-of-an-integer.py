class Solution:
    def punishmentNumber(self, n: int) -> int:
        def backtrack(s, target, total):
            if not s:
                return total == target
            
            for i in range(1, len(s) + 1):
                left = int(s[:i])
                if backtrack(s[i:], target, total + left):
                    return True
            return False

        ans = 0
        for i in range(1, n + 1):
            square = i * i
            if backtrack(str(square), i, 0):
                ans += square
        
        return ans
