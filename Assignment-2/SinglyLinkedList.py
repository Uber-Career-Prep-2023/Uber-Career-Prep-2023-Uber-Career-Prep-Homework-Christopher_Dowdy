# Node class
class Node:
  
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
  
# Linked List class
  
  
class LinkedList:
  
    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None
    def insertAtFront(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        return self.head
    def insertAtBack(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next != None:
            last = last.next
        last.next = newNode
    def insertAfter(self, val, loc):
        newNode = Node(val)
        curr = self.head
        while curr is not None:
            if curr == loc:
                newNode.next = loc.next
                curr.next = newNode
            curr = curr.next
    def deleteFront(self):
        if self.head is None:
            return self.head
        self.head = self.head.next
        return self.head
    def deleteBack(self):
        if self.head is None:
            return self.head
        if self.head.next is None:
            self.head = None
        while self.head.next.next != None:
            self.head = self.head.next
        self.head.next = None
    def deleteNode(self, loc):
        find = self.head
        count = 0
        if loc == 0:
            self.head = self.head.next
            return self.head
        prev, curr = self.head, self.head
        while count != loc:
            prev = curr
            curr = curr.next
            count += 1
        prev.next = curr.next
        return self.head

        return self.head
    def length(self):
        count = 0
        while self.head:
            count+=1
            self.head = self.head.next
        return count
    def reverseIterative(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def reverseRecursive(self,node):
        if not node or not node.next:
            return node
        head = self.reverseRecursive(node.next)
        node.next.next = node
        node.next = None

        return head
