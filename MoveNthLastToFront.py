'''
Intuition:
- To do this without having to iterate through the linked list just to get the length:
    - We could have use fixed distance two pointer approach where the leading pointer starts
    - k distance ahead of the behind pointer
    - once the leading pointer has reached the end of the list, the behind pointer will be at the desired index 
Technique: Fixed-Distance Two-Pointer
TC: O(n) where n is the length of the linked list
SC: O(1)
'''
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def moveNthLastToFront(head,k):
    res = head
    leading = head
    for i in range(k):
        leading = leading.next
    
    trailing = head
    while leading.next:
        trailing = trailing.next
        leading = leading.next
    newHead = trailing.next
    trailing.next = trailing.next.next
    newHead.next = res
    return newHead

#/***********************TESTING****************************/#
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    cur = head
    for val in values[1:]:
        cur.next = Node(val)
        cur = cur.next
    return head

values = [15, 2, 8, 7, 20, 9, 11, 6, 19]
head = create_linked_list(values)
cur = head
while cur:
    print(cur.val, end=' ')
    cur = cur.next

newList = moveNthLastToFront(head, 2)
print("\n")
cur = newList
while cur:
    print(cur.val, end=' ')
    cur = cur.next
'''
Time spent: 20 mins
'''