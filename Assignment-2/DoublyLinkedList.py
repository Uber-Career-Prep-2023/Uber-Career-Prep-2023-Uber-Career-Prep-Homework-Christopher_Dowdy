# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def insertAtFront(self, head, val):
        newNode = Node(val)
        newNode.next = head
        return newNode
    def insertAtBack(self, head, val):
        newNode = Node(val)
        if head is None:
            head = newNode
            return
        last = head
        while last.next != None:
            last = last.next
        last.next = newNode

    def insertAfter(self, head, val, loc):
        newNode = Node(val)
        curr = head
        while curr is not None:
            if curr == loc:
                newNode.next = loc.next
                curr.next = newNode
            curr = curr.next
    def deleteFront(self, head):
        if head is None:
            return head
        head = head.next
        return head
    def deleteBack(self, head):
        if head is None:
            return head
        if head.next is None:
            head = None
        while head.next.next != None:
            head = head.next
        head.next = None

    def deleteNode(self, head, loc):
        count = 0
        if loc == 0:
            head = head.next
            return head
        prev, curr = head, head
        while count != loc:
            prev = curr
            curr = curr.next
            count += 1
        prev.next = curr.next
        return head

    def length(self, head):
        count = 0
        while head:
            count+=1
            head = head.next
        return count
    def reverseIterative(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def reverseRecursive(self, head, node):
        def recursiveHelper(node):
            if not node or not node.next:
                return node
            head = recursiveHelper(node.next)
            node.next.next = node
            node.next = None
            return head

        return recursiveHelper(head)
