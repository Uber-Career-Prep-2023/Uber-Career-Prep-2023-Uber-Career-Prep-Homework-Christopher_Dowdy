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
            letter_index = ord(letter) - 97  # convert letter to index

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

def test_suite():
    test = Trie()
    test.insert("uber")
    assert(test.is_valid_word("uber"))
    test.insert("umbrella")
    assert(test.is_valid_word("umbrella"))
    assert(test.is_valid_word("hi") == False)

    test.remove("uber")
    assert(test.is_valid_word("uber") == False)

test_suite()
