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
    
    def delete(self,val):
        if not self.root:
            return self.root
        
        if self.root.val == val:
            if not self.root.left:
                return self.root.right
            if not self.root.right:
                return self.root.left
            # replace root with its successor if it has two children
            p = self.findSuccessor(self.root)
            self.root.val = p.val
            self.root.right = self.delete(self.root.right,p.val)
            return self.root
        if self.root.val < val:
            self.root.right = self.delete(self.root.right, val)
        else:
            self.root.left = self.delete(self.root.left, val)
        
        return self.root

    def findSuccessor(root):
        # finds the leftmost child in root's right subtree
        curr = root.right
        while curr and curr.left:
            curr = curr.left
        return curr

        