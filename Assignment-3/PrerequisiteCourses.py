'''
graph[Contemporary Literature] = [Intro to Writing]
graph[Ancient Literature] = [Intro to Writing]
graph[Comparitive Literature] = [Ancient literature, Contemporary Literature]

Intuition:
- This can be solved with topological sort
    - remember, this method traverses through a graph by leaf nodes
    - we want to construct an adjacency list with:
        values being pre-req courses
        keys being list of courses unlocked after taking pre-req
Technique: Topological Sort
TC: O(V+E)
SC: O(V+E)
'''

from collections import defaultdict
def PrerequisiteCourses(courses, map):
    leafs = []
    res = []
    adjList = defaultdict(list)
    # need to reconstruct map
    for key,arr in map.items():
        for item in arr:
            adjList[item].append(key)
    # calculate in degrees
    indegrees = {course: 0 for course in courses}
    for node in adjList:
        for neighbor in adjList[node]:
            indegrees[neighbor]+=1
    # populate leafs list
    for node in adjList:
        if indegrees[node] == 0:
            leafs.append(node)
    
    while leafs:
        curr = leafs.pop()
        res.append(curr)

        for node in adjList[curr]:
            indegrees[node]-=1
            if indegrees[node] == 0:
                leafs.append(node)
    return res

def testSuite():
    assert(PrerequisiteCourses(["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"], { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }) == ['Intro to Programming', 'Data Structures', 'Advanced Algorithms', 'Databases', 'Operating Systems'])
    assert(PrerequisiteCourses(["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"], { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }) == ['Intro to Writing', 'Plays & Screenplays', 'Ancient Literature', 'Contemporary Literature', 'Comparative Literature'])
    assert(PrerequisiteCourses([],{}) == [])
    assert(PrerequisiteCourses(["a", "b"], {"a":["b"]}) == ["b","a"])
    assert(PrerequisiteCourses(["a", "b", "c"], {"a": ["b"], "b":["c"]}) == ["c","b","a"])
testSuite() 
"""
Time spent: 30 mins
"""