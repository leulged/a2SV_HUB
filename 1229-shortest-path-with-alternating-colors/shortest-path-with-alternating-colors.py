class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_adj = defaultdict(list)
        blue_adj = defaultdict(list)
        
        for src, dst in redEdges:
            red_adj[src].append(dst)
        for src, dst in blueEdges:
            blue_adj[src].append(dst)
        
        queue = deque()
        queue.append((0, 0))  
        queue.append((0, 1))  
        
        dist = [[float('inf')] * 2 for _ in range(n)]
        dist[0][0] = dist[0][1] = 0  

        while queue:
            node, color = queue.popleft()
            
            if color == 0: 
                for neighbor in blue_adj[node]:
                    if dist[neighbor][1] == float('inf'):
                        dist[neighbor][1] = dist[node][0] + 1
                        queue.append((neighbor, 1))
            else:  
                for neighbor in red_adj[node]:
                    if dist[neighbor][0] == float('inf'):
                        dist[neighbor][0] = dist[node][1] + 1
                        queue.append((neighbor, 0))
        
        answer = []
        for red_dist, blue_dist in dist:
            min_dist = min(red_dist, blue_dist)
            answer.append(min_dist if min_dist != float('inf') else -1)
        
        return answer