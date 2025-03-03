class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sm = 0
        costs.sort(key = lambda x:x[0] - x[1])
        n = len(costs)
        for i in range(n):
            if i < n // 2:
                sm += costs[i][0]
            else:
                sm += costs[i][1]
        return sm