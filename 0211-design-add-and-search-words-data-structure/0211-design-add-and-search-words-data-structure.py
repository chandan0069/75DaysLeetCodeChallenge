class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        
        node.is_end = True

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.root)

    def _dfs(self, word, i, node):
        # base case
        if i == len(word):
            return node.is_end

        ch = word[i]

        # case 1: normal character
        if ch != '.':
            if ch not in node.children:
                return False
            return self._dfs(word, i + 1, node.children[ch])

        # case 2: wildcard '.'
        for child in node.children.values():
            if self._dfs(word, i + 1, child):
                return True
        
        return False