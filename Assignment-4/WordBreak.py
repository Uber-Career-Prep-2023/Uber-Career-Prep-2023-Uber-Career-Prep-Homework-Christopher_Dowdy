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

def word_break(input_string, dictionary):
    dp = [False] * (len(input_string) + 1)
    dp[len(input_string)] = True

    for i in range(len(input_string) - 1, -1, -1):
        for word in dictionary:
            if (i + len(word)) <= len(input_string) and input_string[i:i + len(word)] == word:
                dp[i] = dp[i + len(word)]

    return dp[0]

def test_suite():
    assert word_break("ubereats", ["uber", "eats"])
    assert word_break("uberuber", ["uber", "eats"])
    assert not word_break("ububer", ["uber", "eats"])
    assert not word_break("abe", ["ab", "a", "b"])

test_suite()
