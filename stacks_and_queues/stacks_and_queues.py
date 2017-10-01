class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node

    def pop(self):
        node = self.top
        self.top = node.next
        return node.value

    def peek(self):
        return self.top.value

    def is_empty(self):
        return self.top is None

# 3.1 Three in One: Describe how you could use a single array to implement three stacks.

# With one array and one stack -> pointer to top.
# .pop -> decrement pointer
# .push -> increment pointer
# .is_empty -> pointer at -1

# With one array and two stacks -> two pointers to tops. even index -> 1st stack, odd index -> 2nd stack
# .pop -> decrement pointer by 2
# .push -> increment pointer by 2
# .is_empty -> pointer < 0

# With one array and three stacks -> three pointers to tops.  Pointers increase/decrease by 3.

# 3.2 Stack Min: How would you design a stack with, in addition to push and pop, has a function min
# which returns the minimum element?  Push, pop, and min should all operate in O(1) time.

# push -> check against min and update min if new item is less than min
# pop -> check against min and update min if popped item was minimum
# how to update min without sort O(log n)?
# each node has pointer to min before it?  So when popped, update min pointer with pointer from node


class NodeMin(Node):
    def __init__(self, value, minimum=None):
        self.value = value
        self.next = None
        self.minimum = minimum


class StackMin(Stack):

    def push(self, item):
        node = NodeMin(item)
        node.minimum = node
        if self.top is not None and item >= self.top.minimum.value:
            node.minimum = self.top.minimum
        node.next = self.top
        self.top = node

    def min(self):
        return self.top.minimum.value

# 3.3 Stack of Plates: Imagine a (literal) stack of plates.  If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold.  Implement a data structure SetOfStacks that mimics this.  SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
# that is, pop() should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific sub-stack

# 3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

# 3.5 Sort Stack:  Write a program to sort a stack such that the smallest items are on the top.  You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array).  The stack supports the following operations: push, pop, peek, and isEmpty.

# 3.6 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
# out" basis.  People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type).  They cannot select which specific animal they would like.  Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat.  You may use the build-in LinkedList data structure.
