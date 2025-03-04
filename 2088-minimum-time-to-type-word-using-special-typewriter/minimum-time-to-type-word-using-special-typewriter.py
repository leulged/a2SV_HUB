class Solution:
    def minTimeToType(self, word: str) -> int:
        words = "abcdefghijklmnopqrstuvwxyz"
        word_with_ind = {}
        for i in range(26):
            word_with_ind[words[i]] = i
        
        cnt = len(word)
        curr_ind = 0
        for wrd in word:
            clock = 0
            anticlock = 0
            if curr_ind <= word_with_ind[wrd]:
                clock = word_with_ind[wrd] - curr_ind
                anti_clock = 26 - word_with_ind[wrd] + curr_ind
            else:
                anti_clock = curr_ind -  word_with_ind[wrd] 
                clock = 26 - curr_ind + word_with_ind[wrd]
            cnt += min(clock, anti_clock)
            curr_ind = word_with_ind[wrd]

        return cnt
        