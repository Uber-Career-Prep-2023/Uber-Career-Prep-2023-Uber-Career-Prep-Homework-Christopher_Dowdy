'''
Intuition:
- since we are given recurrence relation, should be a simple to code this up
with dynamic programming (actually for bottom up we have to use a modified recurrence)
f(i) should represent the ith catalan number
- since we want to return a list of the catalan numbers up to n, we can return
the resulting dp array of size n+1
f(0) = 1
f(1) = 1
Technique: Bottom up DP
TC: O(n^2)
SC: O(n)
'''
def CatalanNumbers(n):
    if n == 0:
        return [1]
    dp = [0]*(n+1)
    dp[0],dp[1] = 1,1

    for i in range(2, n+1):
        for j in range(i):
            dp[i]+=dp[j]*dp[i-j-1]
    
    return dp

def testSuite():
    assert(CatalanNumbers(1) == [1,1])
    assert(CatalanNumbers(5) == [1, 1, 2, 5, 14, 42])
    assert(CatalanNumbers(0) == [1])

testSuite()

'''
Time spent: 25 mins
'''