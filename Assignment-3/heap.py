class Heap:
    def __init__(self):
        self.heap = []

    def top(self):
        return self.heap[0]
    
    def insert(self,x):
        self.heap.append(x)
        self.heapifyUp()

    def heapifyUp(self):
        child = len(self.heap) - 1
        parent = (child - 1) // 2

        while parent >= 0 and self.heap[parent] > self.heap[child]:
            self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            child = parent
            parent = (child - 1) // 2

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        root = self.heap.pop()
        self.heapifyDown(0)
        return root

    def heapifyDown(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapifyDown(smallest)

def testSuite():
    h = Heap()

    # Test inserting elements
    h.insert(5)
    assert(h.top() == 5)
    h.insert(3)
    assert(h.top() == 3)
    h.insert(8)
    assert(h.top() == 3)
    h.insert(1)
    assert(h.top() == 1)

    # Test removing elements
    assert(h.remove() == 1)
    assert(h.top() == 3)
    assert(h.remove() == 3)
    assert(h.top() == 5)

    # Test inserting more elements
    h.insert(7)
    assert(h.top() == 5)
    h.insert(2)
    assert(h.top() == 2)
    h.insert(9)
    assert(h.remove() == 2)
    assert(h.remove() == 5)
    

testSuite()