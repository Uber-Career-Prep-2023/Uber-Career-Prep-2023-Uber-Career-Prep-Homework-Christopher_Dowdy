class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.validWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        currNode = self.root

        for letter in word:
            letterIndex = ord(letter)-97 # convert letter to index

            if not currNode.children[letterIndex]:
                newNode = TrieNode()
                currNode.children[letterIndex] = newNode

            currNode = currNode.children[letterIndex]
        currNode.validWord = True
    
    def isValidWord(self, word):
        currNode = self.root

        for letter in word:
            letterIndex = ord(letter)-97

            if not currNode.children[letterIndex]:
                return False
            currNode = currNode.children[letterIndex]
        return currNode.validWord
    
    def isEmpty(self, root):
        for i in range(26):
            if root.children[i]:
                return False
        return True
    
    def remove(self, word):
        def dfs(root,word,depth):
            if not root:
                return None

            if depth == len(word): 
                if root.validWord:
                    root.validWord = False
                if self.isEmpty(root):
                    del root
                    root = None
                return root
            
            index = ord(word[depth])-97
            root.children[index] = dfs(root.children[index], word, depth + 1)

            if self.isEmpty(root) and not root.validWord:
                del root
                root = None
            return root
        
        dfs(self.root,word,0)

def testSuite():
    test = Trie()
    test.insert("uber")
    assert(test.isValidWord("uber"))
    test.insert("umbrella")
    assert(test.isValidWord("umbrella"))
    assert(test.isValidWord("hi") == False)

    test.remove("uber")
    assert(test.isValidWord("uber") == False)

testSuite()


