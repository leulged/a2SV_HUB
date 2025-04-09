class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colors = [-1 for _ in range(n)]
        graph = defaultdict(list)
        
        for x , y in dislikes:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node , color):
            if colors[node - 1] != -1:
                if colors[node - 1] != color:
                    return False

                return True

            colors[node - 1] = color
            
            for child in graph[node]:
                if not dfs(child, 1 - color):
                    return False
            
            return True
            
        for key in range(1 , n + 1):
            if colors[key - 1] == -1:
                if not dfs(key , 1):
                    return False
 
        return True
