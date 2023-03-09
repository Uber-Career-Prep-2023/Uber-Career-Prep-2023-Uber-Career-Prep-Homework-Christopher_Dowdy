'''
Intuition:
- Iterate through the whole array, at each index i of arr calcuate the sum of the arr
up to that index i, add sum to a set
    - if sum at i == 0 or sum exists already in the set, we have found a subarray
    that sums to 0
Technique: One-directional running computation/total
TC: O(n) where n is size of array
SC: O(n) where n is size of array
'''
def ZeroSumSubArrays(arr):
    currSum = 0
    count = 0
    prevSums = set()
    for i in range(len(arr)):
        currSum+=arr[i]
        if currSum == 0 or currSum in prevSums:
            count+=1
        else:
            prevSums.add(currSum)
    return count

def main():
    print(ZeroSumSubArrays([4, 5, 2, -1, -3, -3, 4, 6, -7]) == 2)
    print(ZeroSumSubArrays([1, 8, 7, 3, 11, 9]) == 0)
    print(ZeroSumSubArrays([8, -5, 0, -2, 3, -4]) == 2)
main()
'''
Time spent: 50 mins
'''
