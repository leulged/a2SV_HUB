class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        l = r = 0
        count = 0
        print(s)
        print(g)
        flag = False
        while l < len(g) and r < len(s):
            if s[r] >= g[l]:
                count += 1      
                s[r] -= g[l]
                l += 1
                flag = True

            else:
                if flag:
                    r += 1
                    flag = False
                else:
                    l += 1
            
        return count