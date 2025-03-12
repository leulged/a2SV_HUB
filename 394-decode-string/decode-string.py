class Solution:
    def decodeString(self, s: str) -> str:
        def encode(n, st):
            return st * n

        stack = []
        num = 0
        ans = ""
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((num, ans))
                num = 0
                ans = ""
            elif char == ']':
                n, prev = stack.pop()
                ans = prev + encode(n, ans)
            else:
                ans += char
        
        return ans
