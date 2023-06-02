class Heap:
    def __init__(self):
        self.heap = []
    def top(self):
        return self.heap[0]
    def insert(self,x):
        self.heap.append(x)

        child = len(self.heap)-1
        parent = (child-1)//2

        while parent >= 0 and self.heap[parent] > self.heap[child]:
            self.heap[parent],self.heap[child] = self.heap[child],self.heap[parent]
            child, parent = parent, (child-1)//2
    def remove(self):
        self.heap[0] = self.heap.pop()
        self.heapifyDown(0)
    def heapifyDown(self,i):
        leftChild = 2*i+1
        rightChild = 2*i+2

        if leftChild >= len(self.heap) or rightChild >= len(self.heap):
            return
        smallestChild = i
        if self.heap[leftChild] < self.heap[rightChild]:
            smallestChild = leftChild
        else:
            smallestChild = rightChild
        self.heap[i],self.heap[smallestChild] = self.heap[smallestChild],self.heap[i]
        self.heapifyDown(smallestChild)