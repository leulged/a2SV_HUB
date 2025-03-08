class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        result = 0
        n = len(arr)
        
        left = [0] * n
        right = [0] * n
        
        for i in range(n):
            count = 1
            while stack and arr[stack[-1]] > arr[i]:
                count += left[stack.pop()]
            left[i] = count
            stack.append(i)
        
        stack.clear()
        
        for i in range(n - 1, -1, -1):
            count = 1
            while stack and arr[stack[-1]] >= arr[i]:  
                count += right[stack.pop()]
            right[i] = count
            stack.append(i)
        
        for i in range(n):
            result = (result + arr[i] * left[i] * right[i]) % MOD
        
        return result
