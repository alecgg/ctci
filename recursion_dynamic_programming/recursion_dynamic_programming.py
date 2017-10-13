# 8.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time.  Implement a method to count how many possible ways the child can run up the
# stairs.
from collections import deque


def step_paths(num_steps: int) -> int:
    num_paths = 0
    if num_steps > 1:
        num_paths += 1 + step_paths(num_steps - 1)
    if num_steps > 2:
        num_paths += 1 + step_paths(num_steps - 2)
    if num_steps > 3:
        num_paths += 1 + step_paths(num_steps - 3)
    return num_steps


# 8.2 Robot in a Grid: Imagine a robot sitting on the upper left corner of a grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them.  Design an algorithm to find a path for the robot from the top left to
# the bottom right.
def top_left_to_bottom_right(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    goal = (num_rows - 1, num_cols - 1)
    path = top_left_to_bottom_right_helper(grid, [(0, 0)])
    if path is not None and path[-1] == goal:
        return path
    return None


# could memoize
def top_left_to_bottom_right_helper(grid, path):
    num_rows = len(grid)
    num_cols = len(grid[0])
    goal = (num_rows - 1, num_cols - 1)
    row, col = path[-1]

    # Reached goal
    if (row, col) == goal:
        return path + [(row, col)]

    # Reached off grid or no-no square
    if row >= num_rows or col >= num_cols or not grid[row][col]:
        return path[:]

    # Go right
    right = top_left_to_bottom_right_helper(grid, path + [(row + 1, col)])

    # Go down
    down = top_left_to_bottom_right_helper(grid, path + [(row, col + 1)])

    if right is not None and right[-1] == goal:
        return right

    if down is not None and down[-1] == goal:
        return down

    return None


# 8.3 Magic Index: A magic index in an array A[0...n-1] is defined to be an index such that A[i] =
# i.  Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
# array A.
def magic_index(array):
    return magic_index_helper(array, 0, len(array) - 1)


def magic_index_helper(array, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    if array[mid] == mid:
        return mid
    if mid < array[mid]:
        return magic_index_helper(array, left, mid - 1)
    if mid > array[mid]:
        return magic_index_helper(array, mid + 1, right)


# 8.4 Power Set: Write a method to return all subsets of a set.
def power_set(elements):
    power_set_of_elements = [[]]
    for element in elements:
        new_sets = []
        for set_ in power_set_of_elements:
            new_sets.append(set_ + [element])
        power_set_of_elements.extend(new_sets)
    return power_set_of_elements


# 8.5 Recursive Multiply: Write a recursive function to multiply two positive integers without using the
# * operator.  You can use addition, subtraction, and bit shifting, but you should minimize the
# number of those operations.
def multiply(a, b):
    if a == 1:
        return b
    if b == 1:
        return a
    if a % 2 == 0:
        return multiply(a >> 1, b) << 1
    if b % 2 == 0:
        return multiply(a, b >> 1) << 1
    return a + multiply(a, b - 1)


# 8.6 Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
# different sizes which can slide onto any tower.  The puzzle starts with disks sorted in ascending order
# of size from top to bottom (i.e., each disk sits on top of an even larger one).  You have the following
# constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto another tower.
# (3) A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using stacks.
def towers_of_hanoi(num_disks):
    left, middle, right = deque(range(num_disks)), deque(), deque()
    move_disks(num_disks, start=left, end=right, free=middle)
    return left, middle, right


def move_disks(num_disks, start, end, free):
    # if only one disk, move to goal
    # else, move n - 1 disks to middle
    # 1 disk to right
    # n - 1 disk to right
    if any(sorted(list(d)) != list(d) for d in (start, end, free)):
        raise Exception('OUT OF ORDER!')
    if num_disks == 1:
        end.append(start.pop())
        return
    move_disks(num_disks - 1, start, end=free, free=end)
    move_disks(1, start, end, free)
    move_disks(num_disks - 1, start=free, end=end, free=start)
    return


# 8.7 Permutations without Dups: Write a method to compute all permutations of a string of unique
# characters.
def permutations_without_dups(string):
    if len(string) in (0, 1):
        yield string
        return
    one_less_permutations = permutations_without_dups(string[:-1])
    last_character = string[-1]
    for permutation in one_less_permutations:
        for i in range(len(permutation) + 1):
            yield permutation[:i] + last_character + permutation[i:]


# 8.8 Permutations with Dups: Write a method to compute all permutations of a string whose
# characters are not necessarily unique.  The list of permutations should not have duplicates.
def permutations_with_dups(string, generated_permutations=None):
    if len(string) in (0, 1):
        yield string
        return

    # remember old permutations
    if generated_permutations is None:
        generated_permutations = set()

    one_less_permutations = permutations_with_dups(string[:-1])
    last_character = string[-1]
    for permutation in one_less_permutations:
        for i in range(len(permutation) + 1):
            new_permutation = permutation[:i] + last_character + permutation[i:]
            if new_permutation not in generated_permutations:
                generated_permutations.add(new_permutation)
                yield new_permutation
