class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = list(range(1 , n + 1))
        ans = []
        form = []

        def comb(num):
            if num > n:
                return
            
            if len(form) == k:
                ans.append(form[:])
            
            for i in range(num , len(arr)):
                form.append(arr[i])
                comb(i + 1)
                form.pop()

        comb(0)
        return ans