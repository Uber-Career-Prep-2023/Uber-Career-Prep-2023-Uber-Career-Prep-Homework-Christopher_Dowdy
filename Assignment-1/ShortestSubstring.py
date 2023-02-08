'''
Intuition:
- use a sliding window approach
- store character frequency of second string in map
- set two pointers, second pointer iterates through the first string
  until it find a substring with all the characters from second string
    - contract substring by moving first pointer while substring still contains
     all required characters
- iterate second pointer and repeat process
Technique: shrinking/growing sliding window
TC: not sure about the TC? need help
SC: O(m) where m is the size of string2
'''
from collections import Counter

def ShortestSubstring(s1,s2):
    charFreq = Counter(s2)
    left_pointer = 0
    length = 0
    shortestLength = float('inf')
    for right_pointer in range(len(s1)):
        if s1[right_pointer] in charFreq:
            charFreq[s1[right_pointer]]-=1
        length+=1
        while(all(value < 1 for value in charFreq.values())):
            shortestLength = min(shortestLength,length)
            if s1[left_pointer] in charFreq:
                charFreq[s1[left_pointer]]+=1
            left_pointer+=1
            length-=1
            if (all(value < 1 for value in charFreq.values())):
                shortestLength = min(shortestLength,length)
    return shortestLength

print(ShortestSubstring("abracadabra", "abc"))
print(ShortestSubstring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx"))
print(ShortestSubstring("dog", "god"))
'''
Time spent: 1 hour
'''
