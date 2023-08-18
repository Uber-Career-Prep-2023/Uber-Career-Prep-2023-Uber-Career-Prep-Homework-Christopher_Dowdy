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
    if k == 0:
        return ["0"]
    res = []
    for n in range(k):
        res.append(bin(n)[2:])
    return res

def testSuite():
    assert(FirstKBinaryNumbers(0) == ["0"])
    assert(FirstKBinaryNumbers(1) == ["0"]) 
    assert(FirstKBinaryNumbers(5) == ["0", "1", "10", "11", "100"])
    assert(FirstKBinaryNumbers(10) == ["0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"])

testSuite()
'''
Time spent: 15 mins
'''


