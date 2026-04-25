# import string
def words_count(words: str) -> dict[str, int]: # is not necessary to add a [] in dict
    words = words.lower()

    special_char = ".,'!\"?"

    # counter_dict = {}

    # Remove Special Char
    clear_text = "".join(char for char in words if char not in special_char).split()
    # clear_text = "".join(char for char in words if char not in string.punctuation).split()

    # for char in words:
    #     if char not in special_char:
    #         clear_text += char

    return {word: clear_text.count(word) for word in set(clear_text)}

    # for word in clear_text.split():
    #     counter_dict[word] = counter_dict.get(word, 0) + 1

    # return counter_dict


print(words_count("Python is fun, python is easy!"))
