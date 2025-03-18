class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def find(n , k):
            if n == 1:
                return 0
            
            mid = 2 ** (n - 2)

            if k > mid:
                return 1 - find(n - 1 , k - mid)

            else:
                return find(n - 1 , k)
            
        return find(n , k)

        
