class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        if not s:
            return [[]]
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                nextPartitions = self.partition(s[i:])
                for nextPartition in nextPartitions:
                    found = [s[:i]]
                    found.extend(nextPartition)
                    ans.append(found)
        
        return ans