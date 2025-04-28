class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        visited = [False] * n
        graph = defaultdict(list)

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(nodes , edge_count , node):
            visited[node] = True
            nodes.append(node)
            for neigh in graph[node]:
                edge_count[0] += 1

                if not visited[neigh]:
                    dfs(nodes , edge_count , neigh)



        for i in range(n):
            if not visited[i]:
                edge_count = [0]
                nodes = []
                dfs(nodes , edge_count , i)

                tot_node = len(nodes)
                tot_edge = edge_count[0] // 2
                if (tot_node * (tot_node - 1)) // 2 == tot_edge:
                    ans += 1

        return ans

