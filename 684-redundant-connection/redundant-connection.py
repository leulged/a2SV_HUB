class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = len(edges)

        parent = [i for i in range(size + 1)]
        rank = [0 for i in range(size + 1)]


        def find(x):

            if parent[x] == x:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]
        
        for i in range(size):
                x = edges[i][0]
                y = edges[i][1]
                
                xroot = find(x)
                yroot = find(y)
                
                if xroot != yroot:

                    if rank[xroot] == rank[yroot]:
                        parent[xroot] = yroot
                        rank[yroot] += 1
                        

                    elif rank[xroot] < rank[yroot]:
                        parent[xroot] = yroot
                    
                    else:
                        parent[yroot] = xroot
                        
                else:
                    return [x , y]
                    
        
