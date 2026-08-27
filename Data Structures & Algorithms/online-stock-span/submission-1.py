class StockSpanner:

    def __init__(self):
        self.index = 0
        self.stack = []

    def next(self, price: int) -> int:
        self.index += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        
        prevIndex = 0 if not self.stack else self.stack[-1][1]
        self.stack.append([price, self.index])
        return self.index - prevIndex


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)