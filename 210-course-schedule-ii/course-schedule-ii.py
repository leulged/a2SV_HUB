class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for x , y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        
        queue = deque()
        ans = []
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            ans.append(node)

            for val in graph[node]:
                indegree[val] -= 1
                if indegree[val] == 0:
                    queue.append(val)
                
        if len(ans) != numCourses:
            return []

        return ans
        

        
        

