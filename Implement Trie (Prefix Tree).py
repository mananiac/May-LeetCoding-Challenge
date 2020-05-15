class TrieNode:
    def __init__(self):
        self.is_string = False
        self.leaves = {}
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        cur = self.root
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True
    def search(self, word):
        node = self.childSearch(word)
        if node:
            return node.is_string
        return False        
    def startsWith(self, prefix):
        return self.childSearch(prefix) is not None
    def childSearch(self, word):
        cur = self.root
        for c in word:
            if c in cur.leaves:
                cur = cur.leaves[c]
            else:
                return None
        return cur