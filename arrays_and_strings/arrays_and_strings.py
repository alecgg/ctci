# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


# If I can use a set
def all_unique(string: str) -> bool:
    characters = set()
    for character in string:
        if character in characters:
            return False
        characters.add(string)
    return True


# If I cannot use another data structure
def all_unique_(string: str) -> bool:
    for i in range(len(str) - 1):
        for j in range(i + 1, len(str)):
            if string[i] == string[j]:
                return False
    return True


# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
def is_permutation(string: str, other_string: str) -> bool:
    character_counts = {}
    for character in string:
        character_counts[character] = character_counts.get(character, 0) + 1
    other_character_counts = {}
    for character in other_string:
        other_character_counts[character] = other_character_counts.get(character, 0) + 1
    return character == other_character_counts


# 1.3 URLify: Write a method to replace all spaces in a string with '%20'.  You may assume
# that the string has sufficient space at the end to hold the additional characters, and
# that you are given the "true" length of the string. (Note: If implementing in Java, please
# use a character array so that you can perform this operation in place.)
def urlify(string: str, length: int) -> str:
    # Build URL into list so can emulate in-place behaviour
    url = [None] * length
    for i in range(len(string)):
        url[i] = string[i]

    # Initialize buffer
    buffer = [None, None, None]
    for i in (0, 1, 2):
        buffer[i] = url[i] if i < length else None

    url_i, buffer_i = 0, 0
    while buffer[buffer_i] is not None:
        if buffer[buffer_i] != ' ':
            url[url_i] = buffer[buffer_i]
            buffer[buffer_i] = url[url_i + 3] if url_i + 3 < length else None
            url_i += 1
        else:
            url[url_i] = '%'
            url[url_i + 1] = '2'
            url[url_i + 2] = '0'
            url_i += 3
            buffer[buffer_i] = url[url_i] if url_i < length else None
        buffer_i = (buffer_i + 1) % 3
    return ''.join(url)


# 1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a
# palindrome.  A palindrome is a word or phrase that is the same forwards and backwards.  A permutation
# is a rearrangement of letters.  The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input:    Tact Coa
# Output:   True (permutations: "taco cat", "atco cta", etc.)
def is_palindrome_permutation(string: str) -> bool:
    character_counts = {}
    length = 0
    for character in string.lower():
        if character.isspace():
            continue
        length += 1
        character_counts[character] = character_counts.get(character, 0) + 1
    # if string is even length, then all counts of characters should be even so they mirror each other
    if length % 2 == 0:
        return all(count % 2 == 0 for count in character_counts.values())
    # if string is odd length, then all counts of characters except one (middle) should be even
    return sum(count % 2 == 1 for count in character_counts.values()) == 1


# 1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character.  Given two strings, write a function to check if they are
# one edit (or zero edits) away.
def one_away(string: str, other_string: str) -> bool:
    # same length -> replace only works.  Check if one mismatch
    if len(string) == len(other_string):
        error_count = 0
        for i in range(len(string)):
            if string[i] != other_string[i]:
                error_count += 1
            if error_count > 1:
                return False
        return True
    # length off by one -> only add/remove works check if one mismatch
    elif abs(len(string) - len(other_string)) == 1:
        shorter_string, longer_string = string, other_string
        if len(string) > len(other_string):
            shorter_string, longer_string = other_string, string
        error_count = 0
        for i in range(len(shorter_string)):
            j = i - error_count
            if shorter_string[j] != longer_string[i]:
                error_count += 1
            if error_count > 1:
                return False
        return True
    return False
