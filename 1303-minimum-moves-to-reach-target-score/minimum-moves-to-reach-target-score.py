class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ls = []
        new = target
        for _ in range(maxDoubles):
            new = new // 2
            if new == 0:
                break
            ls.append(new)
        ls.sort()
        
        if not ls:
            return target - 1

        ans = len(ls)
        curr = 1      
        for num in ls:

            if num != curr:
                ans += num - curr

            curr = num * 2

        ans += target - curr

        return ans

