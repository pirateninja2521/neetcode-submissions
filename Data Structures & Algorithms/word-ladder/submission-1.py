class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = defaultdict(list)
        if endWord not in wordList:
            return 0

        def diffOne(word1, word2) -> bool:
            if len(word1) != len(word2): return False
            return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1
        
        def connect(w1, w2):
            adjList[w1].append(w2)
            adjList[w2].append(w1)

        for word in wordList:
            if diffOne(word, beginWord):
                connect(word, beginWord)
            
            for word2 in wordList:
                if diffOne(word, word2):
                    connect(word, word2)
        
        bfsQueue = deque()

        bfsQueue.append((beginWord, 1))

        visited = [beginWord]
        while bfsQueue:
            word, distance = bfsQueue.popleft()
            if word == endWord:
                return distance
            
            for adj in adjList[word]:
                if adj not in visited:
                    visited.append(adj)
                    bfsQueue.append((adj, distance + 1))
        return 0