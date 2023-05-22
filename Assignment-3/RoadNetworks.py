'''
m[Anchorage] = Homer,Copper Center, Healy
m[Homer] = Anchorage
m[Glacier Bay] = Gustavus
m[Gustavus] = Glacier Bay
m[Copper Center] = McCarthy, Anchorage,Fairbanks
m[Fairbanks] = Copper Center, Healy
m[Healy] = Fairbanks, Anchorage

m[Lihue] = Waimea, Princeville
m[Waimea] = Lihue
m[Kona] = Volcano
m[Volcano] = Kona, Hilo
m[Hilo] = Volcano
m[Lahaina] = Hana, Kahului
m[Hana] = Lahaina,Haiku
m[Kahului] = Haiku, Lahaina
m[Haiku] = Kahului, hana
m[Princeville] = Lihue

visited = [Kona, Volcano, Hilo]
Lihue, Waimea, Princeville

Kona, Volcano, Hilo

Lahaina, Hana, Kahului, Haiku, 

Intuition:
- Create an adjacency list from the pairs
    - with the key being a town and the value being its connected towns
- this graph will be disconnected, need to do dfs on the graph until all towns are visited
    - keeping track of how many times we do dfs to get our intended output
Technique: Graph DFS
TC: O(V+E)
'''
from collections import defaultdict
def RoadNetworks(roadPairs):
    townList = defaultdict(set)

    for pair in roadPairs:
        townList[pair[0]].add(pair[1])
        townList[pair[1]].add(pair[0])

    visited = set()

    def dfs(start):
        stack = []
        stack.append(start)
        visited.add(start)
        while stack:
            curr = stack.pop()
            neighbors = townList[curr]
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

    count = 0
    for pair in roadPairs:
        if pair[0] not in visited:
            dfs(pair[0])
            count+=1
            if len(visited) == len(townList):
                return count
    return 0

print(RoadNetworks([("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]))
print(RoadNetworks([("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]))
'''
Time spent: 35 mins
'''


