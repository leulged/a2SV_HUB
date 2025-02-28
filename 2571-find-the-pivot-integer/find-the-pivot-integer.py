class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        nums= []
        for i in range(1, n + 1):
            nums.append(i)

        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(n):
            prefix[i] = prefix[i-1] + nums[i] 
        
        for i in range(n):
            if prefix[i] == prefix[-1] - prefix[i-1]:
                return i+1
        return -1


        