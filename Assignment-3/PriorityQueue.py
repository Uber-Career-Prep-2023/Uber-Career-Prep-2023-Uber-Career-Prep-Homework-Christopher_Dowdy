class PriorityQueue:
    def __init__(self):
        self.heap = []

    def top(self):
        if not self.heap:
            return None
        return self.heap[0]

    def insert(self, element, priority):
        self.heap.append((element, priority))
        self.heapifyUp()

    def heapifyUp(self):
        child = len(self.heap) - 1
        parent = (child - 1) // 2

        while parent >= 0 and self.heap[child][1] > self.heap[parent][1]:
            self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            child, parent = parent, (child - 1) // 2

    def remove(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) > 1:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        root = self.heap.pop()
        if self.heap:
            self.heapifyDown(0)
        return root

    def heapifyDown(self, i):
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        largest = i

        if leftChild < len(self.heap) and self.heap[leftChild][1] > self.heap[largest][1]:
            largest = leftChild
        
        if rightChild < len(self.heap) and self.heap[rightChild][1] > self.heap[largest][1]:
            largest = rightChild

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapifyDown(largest)

def testSuite():
    pq = PriorityQueue()

    pq.insert('A', 2)
    assert(pq.top() == ('A', 2))

    pq.insert('B', 5)
    assert(pq.top() == ('B', 5))

    pq.insert('C', 1)
    assert(pq.top() == ('B', 5))

    pq.insert('D', 3)
    assert(pq.top() == ('B', 5))

    assert(pq.remove() == ('B', 5))
    assert(pq.top() == ('D', 3))

    assert(pq.remove() == ('D', 3))
    assert(pq.top() == ('A', 2))

    assert(pq.remove() == ('A', 2))
    assert(pq.top() == ('C', 1))
    assert(pq.remove() == ('C', 1))
    assert(pq.top() is None)
    assert(pq.remove() is None)

testSuite()