class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def power(base , exp):
            if exp == 0:
                return 1
            
            half  = power(base , exp // 2 )
            half = (half * half) % (10 ** 9 + 7)
            if exp % 2 == 1:
                half *= base
            
            return half

        return (power(5, (n + 1)// 2 ) * power(4, (n)// 2 )) % (10 ** 9 + 7)
            
