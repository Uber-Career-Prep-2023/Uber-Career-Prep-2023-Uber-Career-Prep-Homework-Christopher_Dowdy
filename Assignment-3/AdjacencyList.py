from collections import defaultdict
from collections import deque
adjacencySet = defaultdict(set)

def createGraph(list):
    for pair in list:
        adjacencySet[pair[0]].add(pair[1])
        if pair[1] not in adjacencySet:
            adjacencySet[pair[1]] = set()

createGraph([(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)])
print(adjacencySet)

def bfs(start, target):
    q = deque()
    visited = set()
    q.append(start)
    visited.add(start)
    while q:
        curr = q.popleft()
        neighbors = adjacencySet[curr]
        for neighbor in neighbors:
            if neighbor == target:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return False

def dfs(start, target):
    s = []
    visited = set()
    s.append(start)
    visited.add(start)
    while s:
        curr = s.pop()
        neighbors = adjacencySet[curr]
        for neighbor in neighbors:
            if neighbor == target:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                s.append(neighbor)
    return False

print(dfs(1,3))
print(bfs(1,3))
        
