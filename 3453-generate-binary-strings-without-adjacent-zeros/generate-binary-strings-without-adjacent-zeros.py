class Solution:
    def validStrings(self, n: int) -> List[str]:
        option = ["0" , "1"]
        ans = []
        def back(path):
            if len(path) == n:
                ans.append("".join(path))
                return
            
            for opt in option:
                if  path and opt == "0" and path[-1] == "0":
                    continue
                
                path.append(opt)
                back(path)
                path.pop()

        back([])
        return ans
        