from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        node = self.top
        self.top = node.next
        self.size -= 1
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
class SetOfStacks:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.stacks = [Stack()]

    @property
    def stack(self):
        return self.stacks[-1]

    def push(self, item):
        if len(self.stack) == self.capacity:
            stack = Stack()
            self.stacks.append(stack)
        self.stack.push(item)

    def pop(self):
        if self.stack.is_empty():
            self.stacks.pop()
        return self.stack.pop()

    def peek(self):
        return self.stack.peek()

    def is_empty(self):
        return self.stack.is_empty() and len(self.stacks) == 1

    def pop_at(self, index):
        return self.stacks[index].pop()


# 3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
class MyQueue:
    def __init__(self):
        self.left_stack = Stack()
        self.right_stack = Stack()

    def enqueue(self, item):
        self.left_stack.push(item)

    def dequeue(self):
        while not self.left_stack.is_empty():
            self.right_stack.push(self.left_stack.pop())
        out = self.right_stack.pop()
        while not self.right_stack.is_empty():
            self.left_stack.push(self.right_stack.pop())
        return out

    def peek(self):
        while not self.left_stack.is_empty():
            self.right_stack.push(self.left_stack.pop())
        out = self.right_stack.peek()
        while not self.right_stack.is_empty():
            self.left_stack.push(self.right_stack.pop())
        return out

    def is_empty(self):
        return self.left_stack.is_empty()


# 3.5 Sort Stack:  Write a program to sort a stack such that the smallest items are on the top.  You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array).  The stack supports the following operations: push, pop, peek, and isEmpty.
class SortedStack:
    def __init__(self):
        self.stack = Stack()

    def push(self, item):
        if self.stack.is_empty():
            self.stack.push(item)
        else:
            temporary_stack = Stack()
            while not self.stack.is_empty() and item > self.stack.peek():
                temporary_stack.push(self.stack.pop())
            self.stack.push(item)
            while not temporary_stack.is_empty():
                self.stack.push(temporary_stack.pop())

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.peek()

    def is_empty(self):
        return self.stack.is_empty()


# 3.6 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
# out" basis.  People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type).  They cannot select which specific animal they would like.  Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat.  You may use the build-in LinkedList data structure.
class Dog:
    def __init__(self, name='Inca'):
        self.name = name


class Cat:
    def __init__(self, name='Mordecai'):
        self.name = name


class AnimalQueue:
    def __init__(self):
        self.dog_queue = deque()
        self.cat_queue = deque()
        self.ticket = 0

    def enqueue(self, animal):
        self.ticket += 1
        if isinstance(animal, Dog):
            self.dog_queue.append((animal, self.ticket))
        elif isinstance(animal, Cat):
            self.cat_queue.append((animal, self.ticket))

    def dequeue_any(self):
        dog, dog_ticket = None, None
        try:
            dog, dog_ticket = self.dog_queue.popleft()
        except IndexError:
            pass

        cat, cat_ticket = None, None
        try:
            cat, cat_ticket = self.cat_queue.popleft()
        except IndexError:
            pass

        if dog is None:
            animal = cat
        elif cat is None:
            animal = cat
        elif dog_ticket < cat_ticket:
            animal = dog
        else:
            animal = cat

        if animal is not None:
            if animal is dog and cat is not None:
                self.cat_queue.appendleft((cat, cat_ticket))
            elif animal is cat and dog is not None:
                self.dog_queue.appendleft((dog, dog_ticket))
        return animal

    def dequeue_dog(self):
        return self.dog_queue.popleft()[0]

    def dequeue_cat(self):
        return self.cat_queue.popleft()[0]
