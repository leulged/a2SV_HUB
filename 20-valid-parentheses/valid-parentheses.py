class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        my_dic={")":"(","]":"[","}":"{"}
        for i in s:
            if i in my_dic:
                if stack and stack[-1]==my_dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack