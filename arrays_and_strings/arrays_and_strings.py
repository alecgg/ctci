from typing import List, TypeVar

T = TypeVar('T')

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
    for i in range(len(string) - 1):
        for j in range(i + 1, len(string)):
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
    return character_counts == other_character_counts


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
    return ''.join(str(u) for u in url)


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
    # length off by one -> only add/remove works.  Check if one mismatch
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


# 1.6 String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters.  For example, the string aabcccccaaa would become a2b1c5a3.  If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string.  You can assume the string has only uppercase and lowercase letters (a-z).
def compress(string: str) -> str:
    new_string = []
    last_character = None
    last_character_count = 0
    for character in string:
        if character == last_character:
            last_character_count += 1
        elif last_character is not None:
            new_string.append(last_character + str(last_character_count))
            last_character = character
            last_character_count = 1
        else:
            last_character = character
            last_character_count = 1
    # Handle last character
    if last_character is not None:
        new_string.append(last_character + str(last_character_count))
    new_string = ''.join(new_string)
    return new_string if len(new_string) < len(string) else string


# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees.  Can you do this in place?
def rotate_square_matrix(matrix: List[List[T]]) -> List[List[T]]:
    n = len(matrix)
    for row_i in range((n + 1) // 2):
        for col_i in range(row_i, n - 1 - row_i):
            row_one, col_one = row_i, col_i
            row_two, col_two = col_one, (n - (row_one + 1)) % n
            row_three, col_three = col_two, (n - (row_two + 1)) % n
            row_four, col_four = col_three, (n - (row_three + 1)) % n
            one = matrix[row_one][col_one]
            two = matrix[row_two][col_two]
            three = matrix[row_three][col_three]
            four = matrix[row_four][col_four]
            matrix[row_one][col_one] = four
            matrix[row_two][col_two] = one
            matrix[row_three][col_three] = two
            matrix[row_four][col_four] = three
    return matrix


# 1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.
def zero_matrix(matrix: List[List[T]]) -> List[List[T]]:
    m = len(matrix)
    n = len(matrix[0])
    zero_rows = set()
    zero_cols = set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    for zero_row in zero_rows:
        for j in range(n):
            matrix[zero_row][j] = 0
    for zero_col in zero_cols:
        for i in range(m):
            matrix[i][zero_col] = 0
    return matrix


# 1.9 String rotation: Assume you have a method isSubstring which checks if one word is a substring
# of another.  Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
# call to isSubstring (e.g. "waterbottle" is a rotation of "erbottlewat").
def is_rotation(string: str, other_string: str) -> bool:
    pass
