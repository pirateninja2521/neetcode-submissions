class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = defaultdict(list)
        if endWord not in wordList:
            return 0
        
        def process(word):
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adjList[pattern].append(word)
                adjList[word].append(pattern)
            
        process(beginWord)
        for word in wordList:
            process(word)
        
        bfsQueue = deque()
        bfsQueue.append((beginWord, 1))

        visited = set([beginWord])
        while bfsQueue:
            word, distance = bfsQueue.popleft()
            if word == endWord:
                return distance
            
            for adj in adjList[word]:
                for adjadj in adjList[adj]:
                    if adjadj not in visited:
                        visited.add(adjadj)
                        bfsQueue.append((adjadj, distance + 1))
        return 0