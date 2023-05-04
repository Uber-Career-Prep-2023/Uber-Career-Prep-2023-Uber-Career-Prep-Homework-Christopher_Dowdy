'''
Intuition:
- left subtree of node contains only nodes with values < curr node val
- right subtree of node contains only nodes with vals > curr node val
- lets think about this recursively:
    - at a current node, the node must be fit the conditions of a BST not only for its neighbor
    but also the neighbor of that and so on
    - node.left 
    - node.right
Technique: DFS
TC: O(n) where n is # of nodes in tree
SC: O(n) where n is # of nodes in tree
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    
def IsBST(root):
    def dfs(node,nMin,nMax):
        if not node:
            return True
        if not (node.val < nMax and node.val > nMin):
            return False
        return (dfs(node.left,nMin,node.val) 
                and dfs(node.right,node.val,nMax))
    return dfs(root, float('-inf'),float('inf'))

'''
time spent: 30 mins
'''

#/***********************TESTING****************************/#
root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(7)
root1.left.left = TreeNode(2)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(8)
assert IsBST(root1) == True