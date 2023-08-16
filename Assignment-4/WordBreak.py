'''
Intuition:
- can use dp to solve this coming from the thought that brute force we would check
   each substring if it is in the word dictionary.
- f(i) represents a boolean indicating if it is possible to build word
  up to and including i. 
Technique: Bottom-up DP
TC: O(m*n) where m is # of words, n is length of string
SC: O(m*n)
'''

def WordBreak(input,dictionary):
    dp = [False]*(len(input)+1)
    dp[len(input)] = True

    for i in range(len(input)-1,-1,-1):
        for word in dictionary:
            if (i + len(word)) <= len(input) and input[i:i+len(word)] == word:
                dp[i] = dp[i+len(word)]
    
    return dp[0]

def testSuite():
    assert(WordBreak("ubereats",["uber","eats"]))
    assert(WordBreak("uberuber",["uber","eats"]))
    assert(not WordBreak("ububer",["uber","eats"]))
    assert(not WordBreak("abe",["ab","a","b"]))

testSuite()
# Time spent: 1 hr