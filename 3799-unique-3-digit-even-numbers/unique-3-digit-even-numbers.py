class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
        seen = set()
        for i in range(len(digits)):
            
            for j in range(len(digits)):

                for k in range(len(digits)):

                    if i!=j and i!=k and j!=k:
                        sm = digits[i] * 100 + digits[j] * 10 + digits[k]

                        if sm % 2 == 0 and len(str(sm)) == 3:
                            seen.add(sm)
        print(seen)
        return len(seen)

