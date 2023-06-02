'''
Intuition:
- we can use a min heap to solve this question
- first, add the first value of each sorted array to the heap
    - with the corresponding array and its next index (1) added as a tuple to the heap insertion
- while the heap is not empty, get the min value from the heap & add it to the res array
    - if possible, add the next value from the array we just looked at to the heap
Technique: min heap / priority queue
'''

import heapq
from queue import PriorityQueue
def MergeKSortedArrays(arrays):
    heap = []
    res = []
    for arr in arrays:
        if arr:
            heapq.heappush(heap,(arr[0],arr,1))

    while heap:
        val,arr,next = heapq.heappop(heap)
        res.append(val)
        if next < len(arr):
            heapq.heappush(heap, (arr[next],arr,next+1))
    return res
print(MergeKSortedArrays([[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
        



