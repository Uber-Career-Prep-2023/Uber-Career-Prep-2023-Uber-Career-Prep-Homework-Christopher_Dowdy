'''
- Iterating through every value in the array:
    - check if the value is in the set
        - if it is, increment a counter because we found a pair
    - else, add k - value to the set (this is because k = value + value2)
- Technique: Hashing
- TC: O(n) where n is length of array
- SC: O(n) where n is length of array
'''
def TwoSum(arr, k):
    checkSum = set()
    if k%2 == 0:
        checkSum.add(k//2)
    sumCount = 0
    for num in arr:
        if num in checkSum:
            sumCount+=1
        else:
            checkSum.add(k-num)
    return sumCount
'''
arr = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
arr = [4,4,4]
k = 8
set = {9,0,2,7,5,}
sumCount = 2
checkSum[2] = 2
checkSum[7] = 2
'''
def main():
    print(TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1],10)==3)
    print(TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1],8) == 3) #is the hw output incorrect for this?
    print(TwoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6],6) == 5)
    print(TwoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6],1) == 0)  
main()  
'''
Time spent: 30 mins -- unable to debug optimal solution that passes all test cases :(
'''