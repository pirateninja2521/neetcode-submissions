class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_counter = defaultdict(list)
        for string in strs:
            str_counter[frozenset(Counter(string).items())].append(string)
        return list(str_counter.values())