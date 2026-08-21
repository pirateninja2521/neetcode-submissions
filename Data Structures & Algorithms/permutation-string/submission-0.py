class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        s1counter = Counter(s1)

        s2counter = Counter(s2[:len(s1)])

        for i in range(len(s1), len(s2)):
            if s1counter == s2counter: return True
            s2counter[s2[i]] += 1
            s2counter[s2[i - len(s1)]] -= 1

        return s1counter == s2counter
        