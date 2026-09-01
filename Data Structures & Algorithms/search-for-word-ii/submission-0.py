class TrieNode:
    def __init__(self, char = ""):
        self.char = char
        self.next = {}
        self.isEnd = False
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trieHead = TrieNode()
        for word in words:
            curr = trieHead
            for char in word:
                if char not in curr.next:
                    curr.next[char] = TrieNode(char = char)

                curr = curr.next[char]
            curr.isEnd = True
            curr.word = word
        
        m = len(board)
        n = len(board[0])

        visited = [[False] * n for _ in range(m)]
        answers = set()
        def dfs(i, j, trieNode):
            if not 0 <= i < m or not 0 <= j < n or visited[i][j]:
                return
            
            char = board[i][j]

            if char not in trieNode.next:
                return
            newNode = trieNode.next[char]
            
            if newNode.isEnd:
                answers.add(newNode.word)

            visited[i][j] = True
            dfs(i-1, j, newNode)
            dfs(i+1, j, newNode)
            dfs(i, j-1, newNode)
            dfs(i, j+1, newNode)
            visited[i][j] = False
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, trieHead)
        
        return list(answers)