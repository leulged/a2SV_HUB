class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        color = [-1 for _ in range(numCourses)]

        graph = defaultdict(list)

        for x , y in prerequisites:
            graph[x].append(y)
        
        def dfs(node):
            nonlocal cycle

            if cycle:
                return 
            
            color[node] = 1
            
            # if node in graph:
            for neig in graph[node]:
                if color[neig] == -1:
                    dfs(neig)
                
                elif color[neig] == 1:
                    cycle = True
        
            color[node] = 2
        
        cycle = False
        for course in range(numCourses):
            if color[course] == -1:
                dfs(course)
            if cycle:
                break

        return not cycle