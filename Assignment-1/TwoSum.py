'''
- Iterating through every value in the array:
    - check if the value is in the set
        - if it is, increment a counter because we found a pair
    - else, add k - value to the set (this is because k = value + value2)
'''
def TwoSum(arr, k):
    checkSum = {}
    sumCount = 0
    for num in arr:
        if num in checkSum:
            sumCount+= checkSum[num]
            checkSum[num]+=1
        else:
            checkSum[k-num]=1
    return sumCount
'''
arr = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
k = 10
set = {9,0,}
sumCount = 0
'''
print(TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1],10))
print(TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1],8)) #is the hw output incorrect for this?
print(TwoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6],6))
print(TwoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6],1))