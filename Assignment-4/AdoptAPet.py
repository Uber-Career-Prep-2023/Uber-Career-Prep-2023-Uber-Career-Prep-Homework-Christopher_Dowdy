'''
Intuition:
- we can use use two max heaps, one for dogs and one for cats, to solve this problem
- max heaps will allow us to easily retrieve the pet that has had the most time spent in shelter
Technique: Mantain two heaps
TC: O(n + log(n)) where n is # of animals
SC O(n) where n is # of animals
'''
import heapq

def adopt_a_pet(pets, actions):
    dogs, cats = [], []
    res = []

    for name, pet_type, time in pets:
        if pet_type == "dog":
            heapq.heappush(dogs, (-time, name))
        if pet_type == "cat":
            heapq.heappush(cats, (-time, name))
    
    for action in actions:
        if action[1] == "person":
            _, _, pet_type = action
            if pet_type == "dog":
                if len(dogs) > 0:
                    _, name = heapq.heappop(dogs)
                    res.append([name, "dog"])
                elif len(cats) > 0:
                    _, name = heapq.heappop(cats)
                    res.append([name, "cat"])
            elif pet_type == "cat":
                if len(cats) > 0:
                    _, name = heapq.heappop(cats)
                    res.append([name, "cat"])
                elif len(dogs) > 0:
                    _, name = heapq.heappop(dogs)
                    res.append([name, "dog"])
        else:
            name, pet_type = action
            if pet_type == "dog":
                heapq.heappush(dogs, (0, name))
            elif pet_type == "cat":
                heapq.heappush(cats, (0, name))
    
    return res

def test_suite():
    pets = [("Sadie", "dog", 4),
            ("Woof", "cat", 7),
            ("Chirpy", "dog", 2),
            ("Lola", "dog", 1)]

    actions = [
        ("Bob", "person", "dog"),
        ("Floofy", "cat"),
        ("Sally", "person", "cat"),
        ("Ji", "person", "cat"),
        ("Ali", "person", "cat")
    ]
    
    assert adopt_a_pet(pets, actions) == [['Sadie', 'dog'], ['Woof', 'cat'], ['Floofy', 'cat'], ['Chirpy', 'dog']]

test_suite()

# time spent: 30 mins