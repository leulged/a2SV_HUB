class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for word in s:
            if word == "#":
                
                if stack1:
                    stack1.pop()
                
            else:
                stack1.append(word)
        
        for word in t:
            if word == "#":

                if stack2:
                    stack2.pop()
                
            else:
                stack2.append(word)

        return stack1 == stack2
        