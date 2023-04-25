'''
Intuition:
- I think this is just a simple traversal problem (DFS)
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def FloorInBST(root, target):
    floor = 0
    def dfs(root):
        nonlocal floor
        if not root:
            return
        if root.val <= target:
            floor = max(floor, root.val)
            dfs(root.right)
        else:
            dfs(root.left)
    dfs(root)
    return floor

#/***********************TESTING****************************/#
root = Node(10)
root.left = Node(8)
root.right = Node(16)
root.left.right = Node(9)
root.right.left = Node(13)
root.right.right = Node(17)
root.right.right.right = Node(20)

print(FloorInBST(root,15))
'''
Time spent: 7 mins
'''