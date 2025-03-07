class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        
        for char in s:
            if char == "(":
                stack.append("(")
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                    stack.append(1)  
                else:
                    temp_score = 0
                    while stack and stack[-1] != "(":
                        temp_score += stack.pop()
                    
                    if stack and stack[-1] == "(":
                        stack.pop()
                        stack.append(2 * temp_score)  
                    else:
                        stack.append(temp_score)
        
        return sum(stack)  

