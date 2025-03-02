class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        prefix = [0] * 150
        for i in range(len(logs)):
            start = logs[i][0] - 1950 
            end = logs[i][1] - 1950 
            prefix[start] += 1
            prefix[end] += -1

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        
        earliest = 0
        val = 0 
        for i in range(len(prefix)):
            if val < prefix[i]:
                earliest = i + 1950
                val = prefix[i]
                print(earliest , i)

        return earliest

