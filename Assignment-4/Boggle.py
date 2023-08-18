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
        self.children = [None] * 26
        self.valid_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr_node = self.root

        for letter in word:
            letter_index = ord(letter) - 97

            if not curr_node.children[letter_index]:
                new_node = TrieNode()
                curr_node.children[letter_index] = new_node

            curr_node = curr_node.children[letter_index]
        curr_node.valid_word = True
    
    def is_valid_word(self, word):
        curr_node = self.root

        for letter in word:
            letter_index = ord(letter) - 97

            if not curr_node.children[letter_index]:
                return False
            curr_node = curr_node.children[letter_index]
        return curr_node.valid_word
    
    def is_empty(self, root):
        for i in range(26):
            if root.children[i]:
                return False
        return True
    
    def remove(self, word):
        def dfs(root, word, depth):
            if not root:
                return None

            if depth == len(word): 
                if root.valid_word:
                    root.valid_word = False
                if self.is_empty(root):
                    del root
                    root = None
                return root
            
            index = ord(word[depth]) - 97
            root.children[index] = dfs(root.children[index], word, depth + 1)

            if self.is_empty(root) and not root.valid_word:
                del root
                root = None
            return root
        
        dfs(self.root, word, 0)

def boggle(board, words):
    trie = Trie()

    for word in words:
        trie.insert(word)
    
    rows, cols = len(board), len(board[0])
    valid_words, visited = [], set()
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def dfs(r, c, curr_node, word):
        if not curr_node:
            return
        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited:
            return
        
        if curr_node.valid_word:
            valid_words.append(word)
            trie.remove(word)
        
        visited.add((r, c))

        for dr, dc in directions:
            row = r + dr
            col = c + dc

            if row < 0 or row >= rows or col < 0 or col >= cols:
                continue
            index = ord(board[row][col]) - ord("a")
            if curr_node.children[index]:
                dfs(row, col, curr_node.children[index], word + board[row][col])
        
        visited.remove((r, c))
    
    for r in range(rows):
        for c in range(cols):
            index = ord(board[r][c]) - ord("a")
            if trie.root.children[index]:
                dfs(r, c, trie.root.children[index], board[r][c])
    
    return valid_words

def test_suite():
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    assert boggle(board, words) == ["oath", "eat"]

    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]    
    assert boggle(board, words) == []

    board = [["a"]]
    words = ["a"]    
    assert boggle(board, words) == ["a"]

test_suite()

# Time Spent: 1 hr