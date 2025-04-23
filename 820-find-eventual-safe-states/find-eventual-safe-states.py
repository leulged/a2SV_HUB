class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        queue = deque()
        out_degree = [len(graph[i]) for i in range(n)]
        back = defaultdict(list)

        for i in range(n):
            for j in graph[i]:
                back[j].append(i)

        for i in range(n):
            if out_degree[i] == 0:
                queue.append(i)

        safe = [False] * n
        while queue:
            node = queue.popleft()
            safe[node] = True

            for nei in back[node]:
                out_degree[nei] -= 1
                if out_degree[nei] == 0:
                    queue.append(nei)

        return [i for i in range(n) if safe[i]]
