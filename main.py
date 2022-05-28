# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from typing import Counter


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(Counter(word) == Counter(anagram)):
        print("true")
    else:
        print("false")

    return True

word = "listen"
anagram = input("pls tyoe in the anagram of listen ")
find_anagram(word, anagram)

