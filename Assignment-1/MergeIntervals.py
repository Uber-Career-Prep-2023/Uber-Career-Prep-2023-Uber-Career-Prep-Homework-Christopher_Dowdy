'''
Intuition:
- sort pairs in array first
- two pointer approach 
- if pair1[1] >= pair2[0]: overlap
    - set second pointer to pair2, increment second pointer while pair1[1] >= pair2[0]:
Technique: two pointer
TC: O(nlogn) where n is size of arr
SC: O(n) where n is size of arr
'''
'''
Input: [(1, 2), (2, 3), (4, 8), (5, 7), (9, 12)]
Output:  [(1, 3), (4, 8), (9, 12)]
'''


def MergeIntervals(intervalList):
    intervalList.sort(key=lambda x: x[0])
    mergedList = [[intervalList[0][0], intervalList[0][1]]]
    for interval in intervalList:
        if mergedList[-1][1] >= interval[0]:
            mergedList[-1][1] = max(mergedList[-1][1],interval[1])
        else:
            mergedList.append([interval[0], interval[1]])
    return mergedList

print(MergeIntervals([(5, 8), (6, 10), (2, 4), (3, 6)]))
'''
Time spent: 45 mins (could not get working sol.)
'''