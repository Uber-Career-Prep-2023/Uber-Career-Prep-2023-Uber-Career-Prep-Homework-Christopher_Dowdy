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