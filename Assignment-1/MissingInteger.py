'''
Intuition:
- one way would be to store the values of the array in a set.
- check if each value is in the set up to n, returning the missing integer when found
Technique: hash the elements
TC: O(n) where n is size of the arr
SC: O(n) where n is size of the arr since we are creating set data structure
'''
def MissingInteger(arr, n):
    nums = set(arr)
    count = 1
    while count < n+1:
        if count not in nums:
            return count
        count+=1
    return 0

print(MissingInteger([1, 2, 3, 4, 6, 7],7))
print(MissingInteger([1],2))
print(MissingInteger([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12],12))
'''
Time spent: 15 mins
'''
