'''
Intuition:
- We could implement BFS and at each level, have easy access to the leftmost element
Technique: BFS
TC: O(n) where n is # of nodes
SC: O(n) where n is # of nodes
'''
from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def LeftView(root):
    q = deque()
    res = []
    q.append(root)
    q.append(None)
    ok = True

    while len(q) != 0:
        currNode = q.popleft()
        if not currNode:
            ok = True
            if len(q) == 0:
                break
            else:
                q.append(None)
        else:
            if ok:
                res.append(currNode.val)
                ok = False
            left,right = currNode.left, currNode.right
            if left:
                q.append(left)
            if right:
                q.append(right)
    return res
#/***********************TESTING****************************/#
root = Node(7)
root.left = Node(8)
root.right = Node(3)
root.right.left = Node(9)
root.right.right = Node(13)
root.right.left.left = Node(20)
root.right.right.left = Node(14)
root.right.right.left.right = Node(15)

print(LeftView(root))
'''
Time spent: 30 mins
'''



