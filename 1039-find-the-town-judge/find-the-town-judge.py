class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        trusters = set()  
        for a, b in trust:
            graph[b].append(a)  
            trusters.add(a)

        def isJudge(candidate):
            
            return len(graph[candidate]) == n - 1 and candidate not in trusters

        for person in range(1, n + 1):
            if isJudge(person):
                return person

        return -1
