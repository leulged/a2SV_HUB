class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique = set()
        for perm in permutations(digits, 3):
            if perm[0] == 0:
                continue

            if perm[2] %2 != 0:
                continue
            
            unique.add(perm)

        return len(unique)


