class Solution:
    def lastRemaining(self, n: int) -> int:
        def find_rem(left , right , n , exp , flag):
            if n < 3:
                if not flag:
                    return left
                else:
                    return right
            
            if flag:
                left += 2 **exp

                if n % 2 == 1:
                    right -= 2 **exp

            else:
                right -= 2 **exp 

                if n % 2 == 1:
                    left += 2 **exp

            return find_rem(left , right , n //2 , exp + 1, not flag)

        return find_rem(1 , n , n , 0 , True)
                
