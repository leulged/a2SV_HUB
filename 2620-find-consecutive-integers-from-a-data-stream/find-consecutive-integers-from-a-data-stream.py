class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.k = k
        self.n = 0
        self.my_dic = defaultdict(int)
    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.my_dic[self.value] += 1
        self.n += 1
        print(self.my_dic)
        if self.n < self.k:
            return False
        
        while self.n - self.k != 0:
            x = self.queue.popleft()
            self.n -= 1
            if x in self.my_dic:
                self.my_dic[self.value] -= 1
        
        if self.my_dic[self.value] == self.k:
            return True

        return False

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)