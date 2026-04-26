import string


def find_longest_word(sentence: str) -> str | None:

    clean_sentence = ""
    longest_word = ""

     # Remove special charater from the input
    """ Issue with this loop :  Strings are immutable. This creates a new string every loop"""
    # 1st approach
    for char in sentence.lower():
        if char not in string.punctuation:
            clean_sentence += char
            
    # save the longest word in the longest_word vairable
    for word in clean_sentence.split():
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

print(find_longest_word("Python is awesome!@"))

############################## REFACTOR ##############################

def find_longest_word(sentence: str) -> str | None:

    longest_word = ""
    chars = []

    # Remove special charater from the input
    # Better than 1st approach
    for char in sentence.lower():
        if char not in string.punctuation:
            chars.append(char)

    clean_sentence = "".join(chars)

    # save the longest word in the longest_word vairable
    for word in clean_sentence.split():
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


print(find_longest_word("Python is awesome!@"))


############################## REFACTOR ##############################

import string


def find_longest_word(sentence: str) -> str | None:

    return max((word.strip(string.punctuation) for word in sentence.split()),key=len,default=None)


print(find_longest_word("Python is awesome!@"))
