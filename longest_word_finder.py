import string


def find_longest_word(sentence: str) -> str | None:

    clean_sentence = ""
    longest_word = ""

    # Remove special charater from the input
    for word in sentence.lower():
        if word not in string.punctuation:
            clean_sentence += word
            
    # save the longest word in the longest_word vairable
    for word in clean_sentence.split():
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

print(find_longest_word("Python is awesome!@"))


############################## REFACTOR ##############################

import string


def find_longest_word(sentence: str) -> str | None:

    return max(
        (word.strip(string.punctuation) for word in sentence.split()),
        key=len,
        default=None,
    )


print(find_longest_word("Python is awesome!@"))
