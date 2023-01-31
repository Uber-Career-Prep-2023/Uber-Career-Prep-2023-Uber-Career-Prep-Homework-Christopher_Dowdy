'''
Technique: Fixed Sliding Window
Implementation:
- iterate through arr, keep a sliding window. 
- store the max sum of sliding window as it shifts
- After going through arr and finding max sum, return max sum / k
TC: O(n) where n is length of arr
SC: O(1)
'''
def MaxMeanSubArray(arr, k):
    windowStart = 0
    windowSum = 0
    maxSum = 0

    for windowEnd in range(len(arr)):
        windowSum+=arr[windowEnd]
        if windowEnd >= k-1:
            maxSum = max(maxSum, windowSum)
            windowSum-= arr[windowStart]
            windowStart+=1
    return maxSum/k

print(MaxMeanSubArray([4, 5, -3, 2, 6, 1],2))
print(MaxMeanSubArray([4, 5, -3, 2, 6, 1],3))
print(MaxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6],3))
print(MaxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6],4))
'''
Time spent: 25 mins
'''