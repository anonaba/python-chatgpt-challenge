def find_longest_word(sentence: str) -> str | None:

    longest_word = ""

    for word in sentence.split():
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


print(find_longest_word("Python is awesome"))

############################## REFACTOR ##############################

def find_longest_word(sentence: str) -> str | None:
    return max([word for word in sentence.split()], key=len, default=None)


print(find_longest_word("Python is awesome"))
