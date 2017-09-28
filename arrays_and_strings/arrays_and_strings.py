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
