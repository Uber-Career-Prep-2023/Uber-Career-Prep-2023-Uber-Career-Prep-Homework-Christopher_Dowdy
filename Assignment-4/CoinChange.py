'''
Intuition:
looks like a dp problem
- we want f(i) to represent the number of possible ways to make change for a sum totaling to i
f(0) = 1
- for each amount i from the curr coin value to the total amnt, increment dp[i] by dp[i-coin]
Technique: 1-D Dynamic Programming
TC: O(n*m) where n is # of coins and m is amount
SC: O(m) where m is amount
'''

def CoinChange(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] += dp[j - coin]
    
    return dp[amount]

print(CoinChange([2, 5, 10],20))
print(CoinChange([2, 5, 10],15))

# 50 minutes spent