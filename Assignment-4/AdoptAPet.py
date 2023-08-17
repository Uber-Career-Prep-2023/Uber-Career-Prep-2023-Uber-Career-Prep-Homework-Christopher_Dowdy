'''
Intuition:
- we can use use two max heaps, one for dogs and one for cats, to solve this problem
- max heaps will allow us to easily retrieve the pet that has had the most time spent in shelter
Technique: Mantain two heaps
TC: O(n + log(n)) where n is # of animals
SC O(n) where n is # of animals
'''
import heapq
def AdoptAPet(pets,actions):
    dogs,cats = [],[]

    res = []

    for name,type,time in pets:
        if type == "dog":
            heapq.heappush(dogs, (-time,name))
        if type == "cat":
            heapq.heappush(cats,(-time,name))
    
    for action in actions:
        if action[1] == "person":
            _,_,type = action
            if type == "dog":
                if len(dogs) > 0:
                    _, name = heapq.heappop(dogs)
                    res.append([name,"dog"])
                elif len(cats) > 0:
                    _, name = heapq.heappop(cats)
                    res.append([name,"cat"])
            elif type == "cat":
                if len(cats) > 0:
                    _, name = heapq.heappop(cats)
                    res.append([name,"cat"])
                elif len(dogs) > 0:
                    _, name = heapq.heappop(dogs)
                    res.append([name,"dog"])
        else:
            name,type = action
            if type == "dog":
                heapq.heappush(dogs,(0,name))
            elif type == "cat":
                heapq.heappush(cats,(0,name))
    
    return res

def testSuite():
    pets = [("Sadie","dog",4),
        ("Woof","cat",7),
        ("Chirpy","dog",2),
        ("Lola","dog",1)]

    actions = [
        ("Bob", "person", "dog"),
        ("Floofy", "cat"),
        ("Sally", "person", "cat"),
        ("Ji", "person", "cat"),
        ("Ali", "person", "cat")
        ]
    assert(AdoptAPet(pets,actions) == [['Sadie', 'dog'], ['Woof', 'cat'], ['Floofy', 'cat'], ['Chirpy', 'dog']])

# time spent: 30 mins