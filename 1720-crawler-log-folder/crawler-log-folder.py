class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log == "../":

                if stack:
                    stack.pop()

            else:

                if log != "./":
                    stack.append(log)

        return len(stack) 