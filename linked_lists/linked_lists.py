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

    def __len__(self):
        return sum(1 for _ in self)

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
    current = linked_list.head
    while current is not None:
        if current.value in values:
            previous.next = current.next
        else:
            values.add(current.value)
            previous = current
        current = current.next
    return linked_list


def remove_duplicates_in_place(linked_list):
    current = linked_list.head
    while current is not None:
        previous = current
        compare = current.next
        while compare is not None:
            if current.value == compare.value:
                previous.next = compare.next
            else:
                previous = compare
            compare = compare.next
    return linked_list


# 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
def kth_to_last(linked_list, k):
    length = 0
    node = linked_list.head
    while node is not None:
        length += 1
        node = node.next
    node = linked_list.head
    for i in range(length - (k + 1)):
        node = node.next
    return node


# 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (e.g. any node but the
# first and last node, not necessarily in the exact middle of a singly linked list) given only access to
# that node.
# EXAMPLE
# Input: the node c from the linked list a -> b -> c -> d -> e -> f
# Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f
def delete_node(node):
    node.value = node.next.value
    node.next = node.next.next


# 2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x.  If x is contained within the list, the values of x only need
# to be after the elements less than x (see below).  The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
def partition_linked_list(linked_list, x):
    left_list = LinkedList()
    left_tail = left_list.head
    right_list = LinkedList()
    right_tail = right_list.head
    node = linked_list.head
    while node is not None:
        if node.value < x:
            if left_list.head is None:
                left_list.head = node
            else:
                left_tail.next = node
            left_tail = node
        else:
            if right_list.head is None:
                right_list.head = node
            else:
                right_tail.next = node
            right_tail = node
        next_node = node.next
        node.next = None
        node = next_node
    if left_tail is not None:
        left_tail.next = right_list.head
    linked_list.head = left_list.head or right_list.head
    return linked_list


# 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
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
def sum_lists(linked_list, other_linked_list):
    head = linked_list.head
    other_head = other_linked_list.head
    carry = 0
    out_list = LinkedList()
    out_list_tail = out_list.head
    while head is not None and other_head is not None:
        value = head.value + other_head.value + carry
        if value >= 10:
            carry = 1
            value -= 10
        else:
            carry = 0

        node = Node(value)
        if out_list.head is None:
            out_list.head = node
        else:
            out_list_tail.next = node
        out_list_tail = node

        head = head.next
        other_head = other_head.next

    if carry > 0:
        out_list_tail.next = Node(carry)
    return out_list


def sum_lists_reverse(linked_list, other_linked_list):
    exponent = len(linked_list) - 1
    other_exponent = len(other_linked_list) - 1
    value = 0
    other_value = 0
    for node in linked_list:
        value += node.value * 10**exponent
        exponent -= 1
    for node in other_linked_list:
        other_value += node.value * 10**other_exponent
        other_exponent -= 1
    out_list = LinkedList()
    out_value = value + other_value
    while out_value > 0:
        node = Node(out_value % 10)
        out_value //= 10
        node.next = out_list.head
        out_list.head = node
    return out_list


# 2.6 Palindrome: Implement a function to check if a linked list is palindrome.
def is_palindrome(linked_list):
    # could just form array from linked list and then do this like a normal person
    advances = len(linked_list) - 1
    node = linked_list.head
    for i in range(advances // 2):
        compare = node
        for j in range(advances):
            compare = compare.next
        if node.value != compare.value:
            return False
        advances -= 2
        node = node.next
    return True


# 2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect.  Return the
# intersecting node.  Note that the intersection is defined based on reference, not value.  That is, if the kth
# node of the linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.
def intersection(linked_list, other_linked_list):
    for node in linked_list:
        for other_node in other_linked_list:
            if node is other_node:
                return node
    return None


# 2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C [the same C as earlier]
# Output: C

# A B C D E C D E C D E
#       A B C D E C D E C D E
def loop_detection(linked_list):
    nodes = set()
    for node in linked_list:
        if node in nodes:
            return node
        nodes.add(node)
    return None
