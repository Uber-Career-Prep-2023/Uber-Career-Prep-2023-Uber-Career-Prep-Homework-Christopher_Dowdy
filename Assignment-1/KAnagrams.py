'''
Intuition:
- create a map, storing the frequencies of each character of the first string
- go through the second string, if the character exists in the map, subtract one from its frequency
    - if the character doesn't exist, set its frequency to one
- go through the map if more than k frequencies != 0, return False
Changed approach after debug:
- get the frequences of first string in map
- iterate through the second string
    - check if character is in map, if it is not increment a counter
- if counter > k, return false
Technique: Hashing
TC: O(n + m) where n is length of str1 and m is length of str2
SC: O(n), where n is the length of str1
'''
from collections import Counter

def KAnagrams(str1, str2, k):
    charFreq = Counter(str1)
    changes = 0
    for c in str2:
        if c not in charFreq or charFreq[c] == 0:
            changes+=1
        else:
            charFreq[c]-=1
        if changes > k:
            return False
    return True

print(KAnagrams("apple", "peach",1))
print(KAnagrams("apple", "peach",2))
print(KAnagrams("cat", "dog",3))
print(KAnagrams("debit curd", "bad credit",1))
print(KAnagrams("baseball", "basketball",2)) #shouldn't this out put true because you change at most 2 characters?
'''
Time spent: 25 mins
'''