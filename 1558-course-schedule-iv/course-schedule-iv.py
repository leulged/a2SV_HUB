from collections import defaultdict, deque
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        # Create the prerequisite matrix
        preq = [[False] * numCourses for _ in range(numCourses)]

        # Build graph and track indegrees
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
            preq[u][v] = True  # Direct prerequisite

        # Topological sort
        queue = deque(i for i in range(numCourses) if indegree[i] == 0)

        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                
                for i in range(numCourses):
                    if preq[i][curr]:  # if i is a prerequisite of curr
                        preq[i][neighbor] = True
                  # Also keep the direct one
                preq[curr][neighbor] = True
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Answer queries using the matrix
        ans = []
        for u, v in queries:
            ans.append(preq[u][v])

        return ans
