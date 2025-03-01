class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        cnt = {}
        for i in range(len(mat)):
            c = mat[i].count(1)
            cnt[i] = c
        
        ans = -1
        ind = 0
        print(cnt)
        for key, val in cnt.items():
            if val > ans:
                
                ans = val
                ind = key
        return [ind, ans]
        
        