class TrieNode:
    def __init__(self, char: str = "", isEnd: bool = False):
        self.char = char
        self.children = {}
        self.isEnd = isEnd

class WordDictionary:
    def __init__(self):
        self.start = TrieNode(isEnd = True)

    def addWord(self, word: str) -> None:
        cur = self.start
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char, False)
            cur = cur.children[char]
        cur.isEnd = True

    def search(self, word: str, head: TrieNode = None) -> bool:
        cur = self.start if not head else head
        for idx, char in enumerate(word):
            if char == '.':
                if not cur.children:
                    return False
                res = False
                for node in cur.children.values():
                    res = res or self.search(word[idx+1:], node)
                return res
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.isEnd
