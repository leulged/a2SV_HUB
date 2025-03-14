class Solution:
    def kthCharacter(self, k: int) -> str:
        a = "abcdefghijklmnopqrstuvwxyz"
        cnt = {a[i]: i for i in range(26)}

        s = "a"

        while len(s) < k:
            for ch in s:
                new_s = a[(cnt[ch] + 1) % 26]
                s += new_s
        
        return s[k - 1]
