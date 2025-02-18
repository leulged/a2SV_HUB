class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prefix = [1] 
    
    def add(self, num: int) -> None:
        if num == 0:
            self.nums = []
            self.prefix = [1]
        else:
            self.nums.append(num)
            self.prefix.append(self.prefix[-1] * num)
    
    def getProduct(self, k: int) -> int:
        if len(self.nums) < k:
            return 0
            
        return self.prefix[-1] // self.prefix[-k-1]
