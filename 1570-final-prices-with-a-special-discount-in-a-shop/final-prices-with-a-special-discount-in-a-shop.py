class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ind = []
        
        for i in range(len(prices)):
            if stack:

                while stack and stack[-1] >= prices[i]:
                    prices[ind[-1]] = stack[-1] - prices[i]
                    stack.pop()
                    ind.pop()

                ind.append(i)
                stack.append(prices[i])
                
            else:
                ind.append(i)
                stack.append(prices[i])

        return prices




        