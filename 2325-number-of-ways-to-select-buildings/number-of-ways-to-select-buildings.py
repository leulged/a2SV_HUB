class Solution:
    def numberOfWays(self, s: str) -> int:
        
        n = len(s)
        
        count0, count1 = [0] * n, [0] * n
        
        for i in range(n):
            if i > 0:
                count0[i] = count0[i - 1]
                count1[i] = count1[i - 1]
            
            if s[i] == '0':
                count0[i] += 1
            else:
                count1[i] += 1

        total_0, total_1 = count0[-1], count1[-1]
        valid_count = 0

        for j in range(1, n - 1):
            if s[j] == '0':  
                valid_count += count1[j - 1] * (total_1 - count1[j])
            else: 
                valid_count += count0[j - 1] * (total_0 - count0[j])

        return valid_count

