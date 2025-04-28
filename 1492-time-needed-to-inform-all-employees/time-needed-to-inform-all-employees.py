class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        graph = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        
        queue = deque()
        queue.append((headID, 0))  
        ans = 0
        
        while queue:
            node, time = queue.popleft()
            ans = max(ans, time)
            
            for emp in graph[node]:
                queue.append((emp, time + informTime[node]))
        
        return ans
