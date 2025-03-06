class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = 0
        stack = []
        oper = "+/*-"

        for num in tokens:
            if num not in oper:
                stack.append(int(num))
                
            else:
                curr = 0
                if num == "*":
                    curr += stack[-1] * stack[-2]
                    
                elif num == "+":
                    curr += stack[-1] + stack[-2]
                
                elif num == "/":
                    curr += int(stack[-2] / stack[-1])
                              
                else:
                    curr += stack[-2] - stack[-1]
                
                stack.pop()
                stack.pop()
                stack.append(curr)

        return stack[-1]        