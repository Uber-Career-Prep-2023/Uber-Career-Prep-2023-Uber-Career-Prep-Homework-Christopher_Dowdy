'''
Technique: Forward/backward two pointer
Intuition:
- two pointers at the start and end of string
- if one of the pointers is a vowel:
    - increment other pointer until a vowel is found or pointers cross paths
    - swap vowels
- run until pointers cross
* keep in mind that characters are case sensative
TC: O(n) where n is size of string
SC: O(1) b/c no additional space used besides set which is constant size?
'''
def ReverseVowels(str):
    l,r = 0, len(str)-1
    vowels = set(["a", "e","i","o","u"])
    while l < r:
        if str[l].lower() in vowels:
            while str[r].lower() not in vowels:
                r-=1
            if l < r:
                str = str[:l]+str[r]+str[l+1:r]+str[l]+str[r+1:]
        elif str[r].lower() in vowels:
            while str[l].lower() not in vowels:
                l+=1
            if l < r:
                str = str[:l]+str[r]+str[l+1:r]+str[l]+str[r+1:]
        l+=1
        r-=1
    return str

print(ReverseVowels("Uber Career Prep"))
print(ReverseVowels("xyz"))
print(ReverseVowels("flamingo"))
'''
Time spent: 30 mins
'''
