'''
Intuition:
- build a tree from the words in the dictionary
- traverse through each cell in the board and make a recursive call
   if there is a word in the dictionary that starts with the letter in the cell
- at each call, explore neighbor cells, & check if sequence of letters match word in dict
Technique: Trie and DFS
TC: O(m*n*t) where m in # of rows, n # of cols, and t # of words (not too sure)
SC: O(s) where s is size of trie of words (not too sure)
'''

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

def Boggle(board, words):
    trie = Trie()

    for word in words:
        trie.insert(word)
    
    rows, cols = len(board), len(board[0])
    validWords, visited = [], set()
    directions = [(-1,0),(1,0),(0,1),(0,-1)]

    def dfs(r, c, currNode, word):
        if not currNode:
            return
        if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited:
            return
        
        if currNode.validWord:
            validWords.append(word)
            trie.remove(word)
        
        visited.add((r,c))

        for dr,dc in directions:
            row = r+dr
            col = c+dc

            if row < 0 or row >= rows or col < 0 or col >=cols:
                continue
            index = ord(board[row][col])-ord("a")
            if currNode.children[index]:
                dfs(row,col,currNode.children[index],word+board[row][col])
        
        visited.remove((r,c))
    
    for r in range(rows):
        for c in range(cols):
            index = ord(board[r][c])-ord("a")
            if trie.root.children[index]:
                dfs(r,c,trie.root.children[index],board[r][c])
    
    return validWords

def testSuite():
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    assert(Boggle(board, words) == ["oath","eat"])

    board = [["a","b"],["c","d"]]
    words = ["abcb"]    
    assert(Boggle(board, words) == [])

    board = [["a"]]
    words = ["a"]    
    assert(Boggle(board, words) == ["a"])

testSuite()

# Time Spent: 1 hr