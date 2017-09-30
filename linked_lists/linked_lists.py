class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __iter__(self):
        next_node = self.next
        while next_node is not None:
            yield next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            head = self.head
            previous = None
            while head is not None:
                previous = head
                head = head.next
            previous.next = node

    def __iter__(self):
        head = self.head
        while head is not None:
            yield head
            head = head.next


# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
def remove_duplicates(linked_list):
    values = set()
    previous = None
    for node in linked_list:
        if node.value in values:
            previous.next = node.next
        values.add(node.value)
        previous = node
    return linked_list


def remove_duplicates_in_place(linked_list):
    for node in linked_list:
        previous = node
        for next_node in node:
            if node.value == next_node.value:
                previous.next = next_node.next
            previous = next_node
    return linked_list

1
5
7
2
3
8
4
2
6
9

1
5
7
2
3
8
4
4
6
9
2

# 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

# 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (e.e, any node but the
# first and last node, not necessarily in the exact middle of a singly linked list, given only access to
# that node.
# EXAMPLE
# Input: the node c from the linked list a ->b ->c ->d ->e ->f
# Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f

# 2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x.  If x is contained within the list, the values of x only need
# to be after the elements less than x (see below).  The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

# 2.5 Sum Lists: You have two numbers represented bya  linked list, where each node contains a single
# digit.  The digits are stored in reverse order, such that the 1's digit is at the head of the list.  Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2).  That is, 617 + 295.
# Output: 2-> 1 -> 9.  That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order.  Repeat the above problem.
# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).  That is, 617 + 295.
# Output: 9 -> 1 -> 2.  That is, 912.


# 2.6 Palindrome: Implement a function to check if a linked list is palindrome.

# 2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect.  Return the
# intersecting node.  Note that the intersection is defined based on reference, not value.  That is, if the kth
# node of the linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

# 2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C [the same C as earlier]
# Output: C
