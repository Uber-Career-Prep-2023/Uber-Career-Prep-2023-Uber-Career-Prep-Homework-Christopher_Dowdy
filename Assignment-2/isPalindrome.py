'''
Intuition:
- since for doubly linked list we get head and tail, we can have pointer at start and end of list
    - if their values are not equal, return false
    - else, shift pointers
    - but, how will we know when to end the loop?
        - I guess we can just go to they reach nullptr, may be able to optimize later
Technique: Doubly linked list forward-backward two-pointer
TC: O(n) where n is nodes in list
SC: O(1)
'''
class DoublyNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.tail = None

def isPalindrome(head):
    l,r = head,head.tail

    while l != r:
        if l.val == r.val:
            l = l.next
            r = r.prev
        else:
            return False
    return True

#/***********************TESTING****************************/#

def create_doubly_linked_list(values):
    if not values:
        return None
    head = DoublyNode(values[0])
    prev = head
    for val in values[1:]:
        cur = DoublyNode(val, prev)
        prev.next = cur
        prev = cur
    return head
values = [9, 2, 4, 4, 2, 9]
head = create_doubly_linked_list(values)
cur = head
while cur.next:
    cur = cur.next
head.tail = cur

cur = head
while cur:
    print(cur.val, end=' ')
    cur = cur.next
print()

print(isPalindrome(head))
'''
Time spent: 10 mins
'''