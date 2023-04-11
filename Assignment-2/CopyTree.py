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