# 5.1 Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and
# j.  Write a method to insert M into N such that M starts at bit j and ends at bit i.  You
# can assume that the bits j through i have enough space to fit all of M.  That is, if
# M = 10011, you can assume that there are at least 5 bits between j and i.  You would not, for
# example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.


def insert(n: int, m: int, i: int, j: int) -> int:
    length = 32
    # n        m   i   j
    # 00011111 00  1   3 ->  10001?
    # Clear space in n for m of size j - i + 1 at positions [i, j] (part the sea)
    # shift n left by j - i + 1 and mask off area of the insertion and right of the insertion
    # nnnn----
    # -------n  mask off insertion area plus and area left of insertion
    # ----mmm-  shift m left by j - i + 1 positions
    # nnnnmmmn combine!
    left = n << (j - i + 1)
    left = left & (-1 << j)

    right = n & ~(-1 << i)

    middle = m << j - i + 1

    return left | middle | right


# 5.2 Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, print
# the binary representation.  If the number cannot be represented accurately in binary with at most 32
# characters, print "ERROR."
def binary_to_string(number: float) -> str:
    # OK so 0.72 to 0.0101010101
    # read that incorrectly
    # 0.72 = (7 * 10^-1) + (2 * 10^-2) + (0 * 10^-3) + ...

    # 9 = 9 * 10^0
    # 9 = 1001 <- what's the algorithm?
    # subtract max power of two < number
    # add 1 to digit
    # repeat
    string = ['0', '.']
    for power in range(-1, -33, -1):
        digit = '0'
        if number - 2**power >= 0.0:
            digit = '1'
            number -= 2**power
        string.append(digit)
    if number > 0.0:
        return 'ERROR'
    return ''.join(string)


# 5.3 Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1.  Write code to
# find the length of the longest sequence of 1s you could create.
def longest_one_run(integer: int) -> int:
    # length if 0 surrounded by 1s = left run + 1 + right run
    # length if 0 has 1 on left = left run + 1
    # length if 0 has 1 on right = 1 + right run
    maximum = 0
    with_swap = 0
    without_swap = 0
    for i in range(32):
        last_digit = integer & 0b1
        integer >>= 1
        if last_digit is 1:
            with_swap += 1
            without_swap += 1
        elif last_digit is 0:
            with_swap = without_swap + 1
            without_swap = 0
        maximum = max([maximum, with_swap, without_swap])
    return maximum


# 5.4 Next Number: Given a positive integer, print the next smallest and the next largest number that
# have the same number of 1 bits in their binary representation.
def next_number(integer: int) -> bin:
    # 0001 -> 0000 -> 0000 -> 0001

    # 1001 -> 1000 -> 0100 -> 0110

    # 0011 -> 0010 -> 0001 -> 0011
    # 1100 -> 1010
    # 0101 -> 0100 -> 0010 -> 0011
    # 1001 -> 1000 -> 0100 -> 0110

    # 0111 -> 0110 -> 0101 -> 0111
    # 1110 -> 1101
    # 1011 -> 1010 -> 0110 -> 0111
    # 1101 -> 1100 -> 1010 -> 1011

    # swap rightmost 10
    # if falls off:
    #   swap rightmost 10
    #   turn leftmost zero to right of swap or swap spot to a 1

    # 1001 -> 1010
    # 0011 -> 0101
    # 1100 -> 1100
    # 0101 -> 0110
    # 1001 -> 1010

    # 0111 -> 1011
    # 1110 -> 1110
    # 1011 -> 1101
    # 1101 -> 1110

    # 01100 -> 10|100
    # 01011 -> 01101

    # 01110 -> 10|110 -> 10|110 -> 10|110 -> 10|000 -> 10|011
    #             001 ->    011 ->    011 -> 10|011

    # swap rightmost 01
    # if most significant bit is swapped: <- how to tell?
    # mask & number != 0? where mask = 1s until bit swapped

    zero_one = 0b01
    mask = 0b11
    most_signficant_bit_mask = 0b1
    most_signficant_bit_swapped = False
    for i in range(31):
        if (integer & mask) ^ zero_one is 0b0:
            if (integer & ~most_signficant_bit_mask) is 0b0:
                return integer ^ mask
            else:
                most_signficant_bit_swapped = True
                break
        zero_one <<= 1
        mask <<= 1
        most_signficant_bit_mask = (most_signficant_bit_mask << 1) | 0b1

    if most_signficant_bit_swapped:
        ones = 0b0
        mask = 0b1
        for j in range(i):
            if integer & mask is not 0b0:
                ones |= 1
                ones <<= 1
        return (integer & ~mask) | ones
    return integer

# 5.5 Debugger: Explain what the following code does: ((n & (n - 1)) == 0)


# 5.6 Conversion: Write a function to determine the number of bits you would need to flip to convert
# integer A to integer B.
def num_flips(a: int, b: int) -> int:
    pass

# 5.7 Pairwise swap.  Write a program to swap odd and even bits in an integer with as few instructions as
# possible.  (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).

# 5.8 Draw Line: A monochrome screen is stored as a single array of bytes, allowing eight consecutive
# pixels to be stored in one byte.  THe screen has width w, where w is divisible by 8 (that is, no byte will
# be split across rows).  The height of the screen, of course, can be derived from the length of the array
# and the width.  Implement a function that draws a horizontal line from (x1, y) to (x2, y).
# The method signature should look something like this:
# drawLine(byte[] screen, int width, int x1, int x2, int y)
