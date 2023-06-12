'''
Intuition:
- Interate through range of given number k, at each index, use python
binary conversion to get desired format
- Unsure of a different way without using python library
Technique: String parse
TC: O(k)
SC: O(k)
'''

def FirstKBinaryNumbers(k):
    res = []
    for n in range(k):
        res.append(bin(n)[2:])
    return res

print(FirstKBinaryNumbers(5))
'''
Time spent: 15 mins
'''


