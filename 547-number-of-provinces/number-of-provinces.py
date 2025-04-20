class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited.add(city)
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        n = len(isConnected)
        visited = set()
        provinces = 0

        for city in range(n):
            if city not in visited:
                dfs(city)
                provinces += 1
        
        return provinces
