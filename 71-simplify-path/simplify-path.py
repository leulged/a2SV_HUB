class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        
        for pth in path:
            if pth == "..":
                if stack:
                    stack.pop()

            elif pth != "" and pth != ".":
                stack.append(pth)

        ans ="/" + '/'.join(stack) 

        return ans 
        

        