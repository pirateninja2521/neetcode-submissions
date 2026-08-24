class Solution:
    def __init__(self):
        # Initialize an instance-level dictionary to avoid leaking state between tests
        self.memory = {}

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        if not s:
            return [[]]
        if s in self.memory:
            return self.memory[s]
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                nextPartitions = self.partition(s[i:])
                for nextPartition in nextPartitions:
                    found = [s[:i]]
                    found.extend(nextPartition)
                    ans.append(found)
        
        self.memory[s] = ans
        return ans