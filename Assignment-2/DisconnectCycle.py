'''
Intuition:
- to detect a cycle, we can use slow/fast pointer to iterate through the list.
    - if s == l, then we have a cycle
- the hard part of this problem will be disconnecting the cycle
    - how will we know when to disconnect?
    - not sure how to do this with s/f pointer
- Instead of using s/f pointer, we can hash the nodes while iterating
    - if a duplicate node is found, then we found a cycle 
    - and we just need to set the prev.next = none
Technique: Hash the nodes
TC: O(n) where n is # of nodes
SC: O(n) where n is # of nodes

question for mentor: is there a better sol. with O(1) space?
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.tail = None

def DisconnectCycle(head):
    prev = None
    curr = head
    dupCheck = set()

    while curr:
        if curr in dupCheck:
            prev.next = None
            break
        else:
            dupCheck.add(curr)
            prev = curr
            curr = curr.next
    return head

'''
Time spent: 30 mins
'''
#/***********************TESTING****************************/#

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = head1.next
result1 = DisconnectCycle(head1)
assert result1.val == 1
assert result1.next.val == 2
assert result1.next.next.val == 3
assert result1.next.next.next.val == 4
assert result1.next.next.next.next == None