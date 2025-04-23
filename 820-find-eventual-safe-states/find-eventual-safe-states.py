class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        out_degree = [0] * n
        safe = [False for _ in range(n)]
        for u in range(n):
            out_degree[u] = len(graph[u])
            for v in graph[u]:
                reverse_graph[v].append(u)
        
        queue = deque()
        for i in range(len(out_degree)):
            if out_degree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            safe[node] = True
            for nei in reverse_graph[node]:
                out_degree[nei] -= 1
                if out_degree[nei] == 0:
                    queue.append(nei)
        
        return [i for i in range(n) if safe[i] == True]