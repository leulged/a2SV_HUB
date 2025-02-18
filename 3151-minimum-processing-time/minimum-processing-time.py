class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        ind=0
        minimum=0
        for i in range(len(processorTime)):
            minimum = max(minimum, tasks[ind] + processorTime[i])
            ind+=4

        return minimum