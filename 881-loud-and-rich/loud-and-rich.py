class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for rich, poor in richer:
            graph[rich].append(poor)
            in_degree[poor] += 1
        
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        ans = list(range(n))  
        
        while queue:
            person = queue.popleft()
            
            for neighbor in graph[person]:
                if quiet[ans[person]] < quiet[ans[neighbor]]:
                    ans[neighbor] = ans[person]  
                
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return ans
