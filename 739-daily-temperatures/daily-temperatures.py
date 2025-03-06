class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        ind = []
        ans = [0] * len(temperatures) 
        
        for i in range(len(temperatures)):
            
            if res:

                while res and temperatures[i] > res[-1]:
                    ans[ind[-1]] = i - ind[-1]
                    res.pop()
                    ind.pop()

                res.append(temperatures[i])
                ind.append(i)

            else:
                res.append(temperatures[i])
                ind.append(i)
            
        return ans


