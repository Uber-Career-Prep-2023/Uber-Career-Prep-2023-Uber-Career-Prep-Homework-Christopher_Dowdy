class Heap:
    def __init__(self):
        self.heap = []

    def top(self):
        return self.heap[0]
    
    def insert(self,x):
        self.heap.append(x)
        self.heapifyUp()

    def heapifyUp(self):
        child = len(self.heap)-1
        parent = (child-1)//2

        while parent >= 0 and self.heap[parent] > self.heap[child]:
            self.heap[parent],self.heap[child] = self.heap[child],self.heap[parent]
            child, parent = parent, (child-1)//2

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

    
h = Heap()
h.insert(7)
h.insert(3)
h.insert(9)

print(h.remove())
print(h.remove())
print(h.remove())