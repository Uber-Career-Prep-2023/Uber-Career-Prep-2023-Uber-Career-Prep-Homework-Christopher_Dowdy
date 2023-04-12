'''
Intuition:
- Two pointer linked list approach
- if l == r, shift r while r.next == l, then set l.next = r.next 
Technique: two pointer linked list
TC: O(n) where n is # of nodes
SC: O(1)
'''

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

'''
Time spent: 25 mins
'''