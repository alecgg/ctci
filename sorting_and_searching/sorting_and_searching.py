from bitarray import bitarray


# 10.1 Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
# end to hold B.  Write a method to merge B into A in sorted order
def sorted_merge(array, other_array):
    # can I reference the last element of B that is not a part of the buffer?
    # or do I get the buffer?
    # start at front of both lists
    # compare fronts, and put smaller element into 0 position
    # element in 0 position is not the original element there, move the element to the back of
    # A in the buffer and continue with the buffer element as the next element of the other array
    array_i = array.index(None) - 1
    other_array_i = len(other_array) - 1
    for insertion in range(len(array) - 1, -1, -1):
        value = array[array_i] if array_i >= 0 else None
        other_value = other_array[other_array_i] if other_array_i >= 0 else None

        if value is not None and other_value is not None:
            if value > other_value:
                array[insertion] = value
                array_i -= 1
            else:
                array[insertion] = other_value
                other_array_i -= 1
        elif value is None:
            array[insertion] = other_value
            other_array_i -= 1
        elif other_value is None:
            array[insertion] = value
            array_i -= 1
    return array


# 10.2 Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
# each other.
def anagram_sort(string_array):
    counts = [string_to_count(string) for string in string_array]
    anagrams = []
    for count in counts:
        anagrams.extend([string for string in string_array if count == string_to_count(string)])
        string_array = [string for string in string_array if count != string_to_count(string)]
    return anagrams


def string_to_count(string):
    return {char: string.count(char) for char in string}


# 10.3 Search in a Rotated Array: Given a sorted array of n integers that has been rotated an unknown
# number of times, write code to find an element in the array.  You may assume that the array was
# originally sorted in increasing order.
# EXAMPLE
# Input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
# Output: 8 (the index of 5 in the array)
def rotated_search(element, array):
    # find rotation point by doing a custom binary search
    # then do a normal binary search for the element to be found
    low = 0
    high = len(array) - 1
    inflexion_point = None
    minimum = None
    while inflexion_point is None:
        # Early stop if we find the element
        mid = (low + high) // 2
        value = array[mid]
        if value == element:
            return mid

        minimum = min(m for m in (minimum, value) if m is not None)
        # Reached far-left, comrade
        if mid == 0:
            inflexion_point = 0
        # Found inflexion point
        elif value < array[mid - 1]:
            inflexion_point = mid
        elif mid + 1 < len(array) - 1 and value > array[mid + 1]:
            inflexion_point = mid + 1
        # if value is <= minimum, normal binary search for minimum continues to the left
        elif value <= minimum:
            high = mid - 1
        # otherwise, need to search on the right side because we jumped over the inflexion point
        elif value > minimum:
            low = mid + 1

    # Now normal binary search with fucked up index
    low = 0
    high = len(array) - 1
    print(inflexion_point)
    while low < high:
        mid = (low + high) // 2
        rotated_mid = (mid + inflexion_point) % len(array)
        value = array[rotated_mid]
        if value == element:
            return rotated_mid
        elif value < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# 10.4 Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size
# method.  It does, however, have an elementAt(i) method that returns the element at index i in
# O(1) time.  If i is beyond the bounds of the data structure, it returns -1.  (For this reason, the data
# structure supports only positive integers.)  Given a Listy which contains sorted, positive integers,
# find the index at which an element x occurs.  If x occurs multiple times, you may return any index.
def sorted_search(listy, element):
    # could do a binary search for end of list then do normal binary search for element
    low = 0
    high = 5
    while low < high:
        mid = (low + high) // 2
        # found end
        if listy[mid] >= 0 and listy[mid + 1] == -1:
            break

        if listy[mid] != -1:
            low = mid
        else:
            high = mid

        if listy[high] != -1:
            high *= 2

    # now mid is end of list
    low = 0
    high = mid
    while low < high:
        mid = (low + high) // 2
        if listy[mid] == element:
            return mid
        elif listy[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# 10.5 Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a
# method to find the location of a given string.
# EXAMPLE
# input: ball, {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}}
# output: 4
def sparse_search(string_array, element):
    # binary search with linear scan for actual element instead of empty string
    low = 0
    high = len(element) - 1
    while low < high:
        mid = (low + high) // 2
        string = string_array[mid]

        # scan to the right for an element if we hit empty string
        if not string:
            original_mid = mid
            while not string and mid <= high:
                mid += 1
                string = string_array[mid]
            if mid == high:
                high = original_mid - 1
                continue

        if string == element:
            return mid
        elif string < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# 10.6 Imagine you have a 20GB file with one string per line.  Explain how you would sort the file.

# if I could fit all in memory, just load the file in memory, sort it, and print to file
# if I couldn't fit all in memory, I would load as much of the file as I could into memory,
# sort it, then dump to a temporary file.
# After sorting the whole file into temporary sorted chunks, I would do an n-way merge of the sorted
# chunks to get the original file but sorted out.

# 10.7 Missing int: Given an input file with four billion non-negative integers, provide an algorithm to
# generate an integer that is not contained in the file.  Assume you have 1 GB of memory available for
# this task.
# FOLLOW UP
# What if you only have 10 MB of memory.  Assume that all the values are distinct and we now have
# no more than one billion non-negative integers.
def missing_int(filename):
    # lol, doesn't say it has to be a non-negative integer that you generate ;)
    # in that case, just return -1
    # otherwise, can just generate max(int in file) + 1
    # only need to read file line by line and keep O(1) memory
    maximum = None
    with open(filename) as f:
        for line in f:
            maximum = max(m for m in (maximum, int(line.strip())) if m is not None)
    return maximum + 1


# 10.8 Find Duplicates: You have an array with all the numbers from 1 to N, where N is at most 32,000.  The
# array may have duplicate entries and you do not know what N is.  With only 4 kilobytes of memory
# available, how would you print all duplicate elements in the array?
def find_dups(number_array):
    # bit array -> O(n)
    # or just for loop like normal -> O(n^2)
    # sort and look for dups -> O(n*log n)
    # 4 kilobytes = 32,000 bits
    #
    # make 32,000 bit array
    # foreach number in number array ->
    #   print i if ith bit in bit array is set
    #   set ith bit in bit array
    bits = bitarray(2**32)
    bits.setall(False)
    for number in number_array:
        if bits[number]:
            print(number)
        bits[number] = True
    return


# 10.9 Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in
# ascending order, write a method to find an element.
def sorted_matrix_search(matrix):
    pass

# 10.10 Rank from Stream: Imagine you are reading in a stream of integers.  Periodically you wish to be able
# to look up the rank of a number x (the number of values less than or equal to x).  Implement the data
# structures and algorithms to support the operations.  That is, implement the method track (int
# x), which is called when each number is generated, and the method getRankOfNumber(int
# x), which returns the number of values less than or equal to x(not including x itself).

# 10.11 Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal to
# the adjacent integers and a "valley" is an element which is less than or equal to the adjacent integers.
# For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys.  Given an array
# of integers, sort the array into an alternating sequence of peaks and valleys.
