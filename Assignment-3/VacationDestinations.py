'''
Intuition:
- create undirected, weighted adjacency list to represent the inputs
- traverse the adjacency list starting from the origin 
Technique: graph traversal
TC: O(n+m) 
SC: O(n+m)
'''

from collections import defaultdict, deque
def VacationDestinations(destinations, origin, k):
    adjList = defaultdict(list)
    res = []
    for city1,city2,time in destinations:
        adjList[city1].append((city2,time))
        adjList[city2].append((city1,time))

    q = deque([(origin,-1)])
    visited = set([origin])
    while q:
        curr, time = q.popleft()
     
        if time <= k and time != -1:
            res.append(curr)
        
        for neighbor, newTime in adjList[curr]:
            if neighbor not in visited:
                q.append((neighbor,time+newTime+1))
                visited.add(neighbor)
    return res

def testSuite():
    input = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]
    assert(VacationDestinations(input, "New York",5) == ['Boston', 'Philadelphia'])
    assert(VacationDestinations(input, "New York",7) == ['Boston', 'Philadelphia', 'Newport', 'Washington, D.C.'])
    assert(VacationDestinations(input, "New York",8) == ['Boston', 'Philadelphia', 'Newport', 'Portland', 'Washington, D.C.', "Harper's Ferry"])

    input = [("a", "b", 1), ("b", "c", 2), ("b", "d", 4)]
    assert(VacationDestinations(input, "a",1) == ["b"])
    
testSuite()
'''
Time spent: 20 mins
'''