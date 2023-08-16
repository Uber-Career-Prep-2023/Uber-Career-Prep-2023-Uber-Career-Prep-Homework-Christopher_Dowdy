'''
Intuition:
- I think we can tackle this question with DP b/c there are clear subproblems
- we want f(i) to represent the min cost at the ith stair
- f(i) = cost[i]+min(f(i-1),f(i-2))
- f(0) = 0 bc it costs $0 to be at the start
- f(1) = cost[0] bc we can only climb one step
- f(2) = min(cost[0] + cost[1],cost[1])=> min(cost[1])
Technique: Bottom Up Dynamic Programming
TC: O(n) where n is size of cost arr
TC: O(n) where n is size of cost arr
'''

def MinCostStairClimbing(cost):
    if len(cost) == 1:
        return cost[0]
    if len(cost) == 2:
        return cost[1]
    
    dp = [0]*(len(cost)+1)
    dp[1] = cost[0]
    dp[2] = cost[1]

    for i in range(3,len(cost)+1):
        dp[i] = cost[i-1]+min(dp[i-1],dp[i-2])
    return min(dp[-1],dp[-2])

def testSuite():
    assert(MinCostStairClimbing([4, 1, 6, 3, 5, 8]) == 9)
    assert(MinCostStairClimbing([11, 8, 3, 4, 9, 13, 10]) == 25)
    assert(MinCostStairClimbing([1,100,1,1,1,100,1,1,100,1]) == 6)

testSuite()


'''
Time spent: 15 mins
'''