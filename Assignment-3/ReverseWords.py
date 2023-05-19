'''
Intuition:
- iterate through the sequence of words, adding each word to a stack and ignoring spaces
- then we can pop through the stack adding each word seperated by a space to form the reversed words
Technique: Stack
TC: O(s) where s is the length of the string
SC: O(s) where s is the length of the string 
'''
def ReverseWords(words):
    s = []
    currWord = ""
    for i in range(len(words)):
        if words[i] == " ":
            s.append(currWord)
            currWord = ""
        else:
            currWord+=words[i]
    s.append(currWord)
    res = ""
    while s:
        curr = s.pop()
        if s:
            res = res + curr + " "
        else:
            res = res + curr
    return res
print(ReverseWords("Uber Career Prep"))
print(ReverseWords("Emma lives in Brooklyn, New York."))
'''
15 mins
'''