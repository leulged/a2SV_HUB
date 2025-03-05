class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for word in s:
            if word == "*":

                if stack:
                    stack.pop()

            else:
                stack.append(word)

        return "".join(stack)
        