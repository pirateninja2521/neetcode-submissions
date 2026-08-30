class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.stacks = []

    def push(self, val: int) -> None:
        self.count[val] += 1
        if len(self.stacks) < self.count[val]:
            self.stacks.append([])
        self.stacks[self.count[val] - 1].append(val)

    def pop(self) -> int:
        ans = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        self.count[ans] -= 1
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()