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
def MergeIntervals(intervalList):
    intervalList.sort()
    print(intervalList)
    l,r = 0, 0
    result = []
    while r < len(intervalList)-1:
        l = r
        if intervalList[l][1] >= intervalList[l+1][0]:
            r+=1
            while intervalList[r][1] >= intervalList[r+1][0] and r < len(intervalList)-1:
                r+=1
            if intervalList[l][1] > intervalList[r][1]:
                result.append([intervalList[l][0],intervalList[l][1]])
            else:
                result.append([intervalList[l][0],intervalList[r][1]])
        else:
            result.append([intervalList[l][0],intervalList[l][1]])
        r+=1
    return result
print(MergeIntervals([(5, 8), (6, 10), (2, 4), (3, 6)]))
'''
Time spent: 45 mins (could not get working sol.)
'''