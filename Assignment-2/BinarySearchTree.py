class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    def min(self):
        def search(node):
            if node.left is None:
                return node.data
            return search(node.left)
        return search(self.root)
    
    def max(self):
        def search(node):
            if node.right is None:
                return node.data
            return search(node.right)
        return search(self.root)
    
    def contains(self,val):
        def dfs(node):
            if node is None:
                return False
            if node.data == val:
                return True
            return dfs(node.left) if node.data > val else dfs(node.right)
        return dfs(self.root)
    
    def insert(self,val):
        if not self.root:
            return Node(val)
        if val > self.root.data:
            self.root.right = self.insert(self.root.right,val)
        else:
            self.root.left = self.insert(self.root.left,val)
        return self.root

        