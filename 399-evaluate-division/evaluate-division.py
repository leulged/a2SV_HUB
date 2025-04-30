class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i in range(len(equations)):
            a, b = equations[i]
            value = values[i]
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        ans = [-1.0000 for _ in range(len(queries))] 

        for i in range(len(queries)):
            start = queries[i][0]
            end = queries[i][1]

            visited = set()
            queue = deque([(start, 1.0)])  


            if start not in graph or end not in graph:
                    continue

            while queue:
                node, value = queue.popleft()
         
                for neigh , wei in graph[node]:
                    if neigh == end:
                        ans[i] = wei * value

                    elif neigh not in visited:
                        visited.add(neigh)
                        queue.append((neigh , value * wei))
                        
        return ans
