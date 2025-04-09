"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        visit = set()
        for employee in employees:
            graph[employee.id].append(employee.importance)
            graph[employee.id].append(employee.subordinates)
            
        ans = 0
        def dfs(node):
            nonlocal ans

            if node in visit:
                return 
            visit.add(node)
            ans += graph[node][0]

            for subordinate in graph[node][1]:
                if subordinate not in visit:
                    dfs(subordinate)
                



  
        dfs(id)
        
        return ans