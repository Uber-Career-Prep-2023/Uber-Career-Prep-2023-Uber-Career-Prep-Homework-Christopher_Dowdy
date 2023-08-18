from collections import defaultdict
from collections import deque
adjacencySet = defaultdict(set)

def createGraph(list):
    for pair in list:
        adjacencySet[pair[0]].add(pair[1])
        if pair[1] not in adjacencySet:
            adjacencySet[pair[1]] = set()

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

def topologicalSort():
    indegrees = {node : 0 for node in adjacencySet}
    for node in adjacencySet:
        for neighbor in adjacencySet[node]:
            indegrees[neighbor]+=1
    
    validNodes = []
    for node in indegrees:
        if indegrees[node] == 0:
            validNodes.append(node)
    
    res = []

    while validNodes:
        currNode = validNodes.pop()
        res.append(currNode)

        for neighbor in adjacencySet[currNode]:
            indegrees[neighbor]-=1
            if indegrees[neighbor] == 0:
                validNodes.append(neighbor)
    
    return res

def testSuite():
    # Test createGraph
    createGraph([(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)])
    assert(adjacencySet == {5: {0, 2}, 2: {3}, 0: set(), 4: {0, 1}, 1: set(), 3: {1}})
    
    # Test bfs and dfs
    assert(bfs(5,2) == True)
    assert(dfs(5,2) == True)
    assert(bfs(5,3) == True)
    assert(dfs(5,3) == True)
    assert(bfs(5,4) == False)
    assert(dfs(5,4) == False)
    assert(bfs(2,0) == False)
    assert(dfs(2,0) == False)

    # Test Topological Sort
    assert(topologicalSort() == [4, 5, 2, 3, 1, 0])

testSuite()
