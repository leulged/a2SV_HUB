class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for x, y in edges:
            graph[y].append(x)

        memo = {}

        def dfs(node):
            if node in memo:
                return memo[node]
            
            visited = set()
            for parent in graph[node]:
                visited.add(parent)
                visited.update(dfs(parent))
            
            memo[node] = visited
            return visited

        ans = []
        for i in range(n):
            ancestors = dfs(i)
            ans.append(sorted(ancestors))

        return ans
