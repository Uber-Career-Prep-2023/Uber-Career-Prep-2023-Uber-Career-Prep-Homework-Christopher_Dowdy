'''
graph[A] = [(B,blue),(C,red),(D,red)]
graph[B] = [(D,blue),(E,blue)]
graph[C] = [(B,red)]
graph[D] = [(C,blue),(E,red)]
graph[E] = [(C,red)]

origin = A, destination = E

q = [(D,blue,4),(E,blue,4)]
curr = (B,red,3)

Intuition:
- First, we can create an adjancency list from the given edges
- Then, we can do a modified BFS on the graph to find the shortest path with alternating colors
Technique: BFS
TC: O(n+m) where n is the # of nodes and m is the # of edges
SC: O(n+m)
'''

from collections import defaultdict,deque
def AlternatingPath(edges,origin,dest):
    graph = defaultdict(list)
    for start,end,color in edges:
        graph[start].append((end,color))
    
    q = deque([(origin,None,0)])
    
    while q:
        curr,prevColor,level = q.popleft()

        if curr == dest:
            return level
        
        for neighbor,color in graph[curr]:
            if color != prevColor:
                q.append((neighbor,color,level+1))
    
    return -1

inputEdges = [('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), ('B', 'E', "blue"), ('C', 'B', "red"),
                   ('D', 'C', "blue"), ('A', 'D', "red"),
                   ('D', 'E', "red"), ('E', 'C', "red")]
print(AlternatingPath(inputEdges,'A','E'))
print(AlternatingPath(inputEdges,'E','D'))
'''
Time spent: 30 mins
'''