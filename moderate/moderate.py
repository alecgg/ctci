# 16.1 Number Swapper: Write a function to swap a number in place (that is, without temporary variables).

# 16.2 Word Frequencies: Design a method to find the frequency of a occurrences of any given word in a
# book.  What if we were running this algorithm multiple times?

# 16.3 Intersection: Given two straight line segments (represented as a start point and an end point),
# compute the point of intersection, if any.

# 16.4 Tic Tac Win: Design algorithm to figure out if someone has one a game of tic-tac-toe.

# 16.5 Factorial Zeros: Write an algorithm which computes the number of trailing zeros in n factorial.

# 16.6 Smallest Difference: Given two arrays of integers, compute the pair of values (one value in each
# array with the smallest (non-negative) difference.  Return the difference
# EXAMPLE
# Input: {1, 3, 15, 1, 2}, {23, 127, 235, 19, 8}
# Output: 3, That is, the pair (11, 8).

# 16.7 Number Max: Write a method that finds the maximum of two numbers.  You should not use if-else
# or any other comparison operator.

# 16.8 English Int: Given any integer print an English phrase that describes the integer (e.g., "One thousand
# Two Hundred Thirty Four").

# 16.9 Operations: Write methods to implement the multiply, subtract, and divide operations for integers.
# The result of all of these are integers.  Use only the add operator.

# 16.10 Living People: Given a list of people with their birth and death years, implement a method to
# compute the year with the most number of people alive.  You may assume that all peole were born
# between 1900 and 2000 (inclusive).  If a person was alive during any portion of that year, they should
# be included in that year's count.  For example, Person(birth=1908, death=1909) is included in the
# counts for both 1908 and 1909.

# 16.11 Diving Board: You are building a diving board by placing a bunch of planks of wood end-to-end.
# There are two types of planks, one of length shorter and one of length longer.  You must use
# exactly K planks of wood.  Write a method to generate all possible lengths of the diving board.

# 16.12 XML Encoding: Since the XML is very verbose, you are given a way of encoding it where ach tag gets
# mapped to a pre-defined integer value.  The language/grammar is as follows:
# Element --> Tag Attributes END Children END
# Attribute --> Tag Value
# END --> 0
# Tag --> some predefined mapping to int
# Value --> string value
# For example, the following XML might be converted into the compressed string below (assuming a
# mapping of family -> 1, person -> 2, firstName -> 3, lastName -> 4, state
# -> 5).
# <family lastName="McDowell" state="CA">
#   <person firstName="Gayle">Some Message</person>
# </family>
# Becomes:
# 1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0
# Write code to print the encodes version of an XML element (passed in Element and Attribute
# objects).
