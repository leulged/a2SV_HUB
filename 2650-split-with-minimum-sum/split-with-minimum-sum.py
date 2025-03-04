class Solution:
    def splitNum(self, num: int) -> int:
        ls = [int(i) for i in str(num)]
        ls.sort()

        one = ""
        two = ""
        for i in range(len(ls)):
            if i % 2 == 0:
                one += str(ls[i])

            else:
                two += str(ls[i])
        
        return int(one) + int(two)
        