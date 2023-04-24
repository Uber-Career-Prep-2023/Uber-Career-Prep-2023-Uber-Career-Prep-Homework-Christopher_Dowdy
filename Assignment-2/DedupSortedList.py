'''
Intuition:
- Two pointer linked list approach
- if l == r, shift r while r.next == l, then set l.next = r.next 
Technique: two pointer linked list
TC: O(n) where n is # of nodes
SC: O(1)
'''
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def DedupSortedList(head):
    if not head:
        return head
    l, r = head, head.next
    while r:
        if l.val == r.val:
            while r.next == l:
                r = r.next
            l.next = r.next
            r = r.next
        else:
            l = l.next
            r = r.next
    return head

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

values = [1, 2, 2, 4, 5, 5, 5, 10, 10]
head = create_linked_list(values)
cur = head
while cur:
    print(cur.val, end=' ')
    cur = cur.next

newList = DedupSortedList(head)
print("\n")
cur = newList
while cur:
    print(cur.val, end=' ')
    cur = cur.next
'''
Time spent: 25 mins
'''