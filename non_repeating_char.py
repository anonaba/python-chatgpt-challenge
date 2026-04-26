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


############################## REFACTOR ##############################
"""
Since you are looking for a single value (the first character with a count of 1) rather than a list, you can use a generator expression inside the next() function

⚡ Key Components
(char for char in word if ...): This is a generator. It finds items one by one instead of building a whole list in memory.
next(..., None):
It grabs the very first item that matches your if condition.
The None at the end prevents the code from crashing if no character has a count of 1 (returning None instead of an error).

Why not a List Comprehension?
You could do [char for char in word if count[char] == 1][0], but that is inefficient.
It searches the entire word.
It builds a list of every unique character.
It then throws away everything except the first one.

next() stops the moment it finds a match, making it much faster for long strings.
"""

def non_repeating_char(word: str) -> str | None:
    word = word.lower()

    count = {char: word.count(char) for char in word}
    
    return next((char for char in word if count[char] == 1), None)


print(non_repeating_char("stress"))

