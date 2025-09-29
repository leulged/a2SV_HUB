class Solution:
    def fib(self, n: int) -> int:
        memory = defaultdict(int)
        def fibonnaci (i):
            if i == 0 or i == 1 :
                return i
            
            if memory[i] != 0 :
                return memory[i]
            
            return fibonnaci(i - 1) + fibonnaci(i - 2)
        
        return fibonnaci(n)
        