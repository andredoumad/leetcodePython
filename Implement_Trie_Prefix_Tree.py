# Andre Doumad
# 200908
'''
Implement Trie (Prefix Tree)
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

class Trie:
    def __init__(self):
        self.end = False
        self.c = {}

    def insert(self, word):
        node = self
        for w in word:
            if w not in node.c:
                node.c[w] = Trie()
            node = node.c[w]
        node.end = True
            
    def prefixnode(self,word):
        node = self
        for w in word:
            if w not in node.c:
                return None
            node = node.c[w]
        return node
    
    def search(self, word):
        node = self.prefixnode(word)
        if not node:
            return False
        else:
            return True if node.end else False
            
    def startsWith(self, prefix):
        node = self.prefixnode(prefix)
        return bool(node)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # returns true
print(trie.search("app"))     # returns false
print(trie.startsWith("app")) # returns true
trie.insert("app")   
print(trie.search("app"))     # returns true