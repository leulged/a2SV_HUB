class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x: x[1])
        max_point = nums[-1][1]
        prefix = [0] * (max_point + 2)

        for start, end in nums:
            prefix[start] += 1
            prefix[end + 1] -= 1

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]

        count = 0
        for i in range(len(prefix)):
            if prefix[i] != 0:
                count += 1
        
        return count
        