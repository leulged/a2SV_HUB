class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        rank = [0] * 26

        def find(x):
            if x == parent[x]:
                return x
            
            return find(parent[x])
        
        def union(x, y):
            xr, yr = find(x), find(y)
            if xr != yr:
                if rank[xr] < rank[yr]:
                    parent[xr] = yr
                elif rank[xr] > rank[yr]:
                    parent[yr] = xr
                else:
                    parent[yr] = xr
                    rank[xr] += 1
        
        for eq in equations:
            if eq[1] == '=':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                union(x, y)
        
        for eq in equations:
            if eq[1] == '!':
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                
                if find(x) == find(y):
                    return False
        
        return True