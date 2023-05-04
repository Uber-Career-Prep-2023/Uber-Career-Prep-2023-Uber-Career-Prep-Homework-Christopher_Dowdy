'''
Intuition:
- Recursive dfs approach
    - base case: if root is none, return None
    - create copy of current node, then recursively call node.left and node.right
Technique: DFS traversal, pre-order
TC: O(n) where n is number of nodes in tree
SC: O(n) where n is number of nodes in tree
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def CopyTree(root):
    def dfs(node):
        if node is None:
            return None
        
        newNode = TreeNode(node.val)
        newNode.left = dfs(node.left)
        newNode.right = dfs(node.right)
        
        return newNode
    return dfs(root)
'''
Time spent: 18 mins
'''

#/***********************TESTING****************************/#
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

copied_root = CopyTree(root)

# Verify that the copied tree has the same structure and values as the original tree
assert copied_root.val == root.val
assert copied_root.left.val == root.left.val
assert copied_root.right.val == root.right.val
assert copied_root.left.left.val == root.left.left.val
assert copied_root.left.right.val == root.left.right.val
assert copied_root.right.left.val == root.right.left.val
assert copied_root.right.right.val == root.right.right.val