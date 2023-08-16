'''
Intuition:
- after each new number, sort our current array of numbers
- after sorted, we can find the middle index of the array for the median
Technique: Sorting/Math
TC: O(nlogn) where n is length of number stream
SC: O(n) where n is length of number stream
'''

def RunningMedian(nums):
    store = []
    res = []
    for num in nums:
        store.append(num)
        store.sort()

        n = len(store)

        if n % 2 == 1:
            res.append(store[n//2])
        else:
            res.append((store[n//2-1]+store[n//2])/2.0)

    return res

def testSuite():
    assert(RunningMedian([1,2,3]) == [1,1.5,2.0])
    assert(RunningMedian([1,11,4,15,12]) == [1, 6.0, 4, 7.5, 11])

testSuite()

# time spent: 20 mins