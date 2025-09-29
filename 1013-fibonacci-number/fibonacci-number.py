class Solution:
    def fib(self, n: int) -> int:
        memory = {}
        def fibonnaci (i):
            if i == 0 or i == 1 :
                return i
            
            if i in memory:
                return memory[i]
            
            memory[i] = fibonnaci(i - 1) + fibonnaci(i - 2)
            return memory[i]
            
        return fibonnaci(n)
        