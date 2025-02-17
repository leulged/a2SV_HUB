class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ind=[0]*len(s)
        word="abcdefghijklmnopqrstuvwxyz"
        for start , end , val in shifts:
            if val==0:
                ind[start] += -1
                if end<len(s)-1:
                    ind[end+1] -= -1
            else:
                ind[start] += 1
                if end<len(s)-1:
                    ind[end+1] -=1
        for i in range(1,len(ind)):
            ind[i] += ind[i-1]
            
        ans=""
        for i in range(len(ind)):
            curr = word.index(s[i])
            ans += word[(curr+ind[i])%26]

        return ans