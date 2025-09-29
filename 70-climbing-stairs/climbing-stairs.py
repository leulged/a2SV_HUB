class Solution:
    def climbStairs(self, n: int) -> int:
        
        memory = {}
        def find(i):        
            if i == 1 or i == 0:     
                return 1

            if i in memory:
                return memory[i]
            
            memory[i] = find(i - 1) + find(i - 2)
            return memory[i]
 
        return find(n)
            
