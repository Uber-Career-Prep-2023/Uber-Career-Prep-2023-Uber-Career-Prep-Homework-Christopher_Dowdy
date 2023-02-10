'''
Intuition:
- Iterate through every value in the array:
    - if the value is in the map, delete it from the array 
    - else, add it to the map
^^key modification: subtracting one from incrementor if we delete so that we adjust to the new array size
Technique: hashing
TC: O(n) where n is size of array
SC: O(n) where n is size of array
'''

def DedupArray(arr):
    dupCheck = set()
    i = 0
    while i < len(arr):
        if arr[i] in dupCheck:
            del arr[i]
            i -=1
        else:
            dupCheck.add(arr[i])
        i+=1
    return arr

print(DedupArray([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
print(DedupArray([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]))
print(DedupArray([1, 3, 4, 8, 10, 12]))
'''
Time spent: 15 mins
'''