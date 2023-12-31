"""
Write function RemoveExclamationMarks which removes all
exclamation marks from a given string.
"""


def remove_exclamation_marks(s):
    return s.replace('!', '')


print(remove_exclamation_marks("Hello World!"))  # "Hello World"
print(remove_exclamation_marks("Hello World!!!"))  # "Hello World"
print(remove_exclamation_marks("Hi! Hello!"))  # "Hi Hello"
print(remove_exclamation_marks(""))  # ""
print(remove_exclamation_marks("Oh, no!!!"))  # "Oh, no"
