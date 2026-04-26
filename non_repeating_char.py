# Challenge #3 — Find the First Non-Repeating Character
def non_repeating_char(word: str) -> str | None:
    word = word.lower()

    count = {}

    for char in word:
        count[char] = count.get(char, 0) + 1

    for char in word:
        if count[char] == 1:
            return char

    return None


print(non_repeating_char("stress"))
