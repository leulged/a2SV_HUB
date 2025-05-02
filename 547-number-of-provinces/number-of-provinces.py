class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        parent = [i for i in range(size)]
        rank = [0 for i in range(size)]
        ans = size
        
        def find(x):
        
            if parent[x] == x:
                return x
            
            parent[x] = find(parent[x])
            return find(parent[x])
        
        for i in range(size):
            for j in range(size):

                if isConnected[i][j] == 1:
                    xroot = find(i)
                    yroot = find(j)

                    if xroot != yroot:

                        if rank[xroot] == rank[yroot]:
                            parent[xroot] = yroot
                            rank[yroot] += 1

                        elif rank[xroot] < rank[yroot]:
                            parent[xroot] = yroot
                        
                        else:
                            parent[yroot] = xroot

                        ans -= 1
        
        return ans