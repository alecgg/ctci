from collections import deque


class Edge:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight


class Node:
    def __init__(self, edges=None):
        self.edges = edges
        if edges is None:
            self.edges = []


class DirectedGraph:
    def __init__(self, nodes=None):
        self.nodes = None
        if nodes is None:
            self.nodes = []


class TreeNode:
    pass


class BinaryTree:
    pass


# 4.1 Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
def route_exists(node, other_node):
    frontier = deque([node])
    visited = set()
    while len(frontier) > 0:
        check = frontier.popleft()
        if check is other_node:
            return True
        visited.add(check)
        for edge in check.edges:
            if edge.dest not in frontier and edge.dest not in visited:
                frontier.append(edge.dest)
    return False


# 4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an
# algorithm to create a binary search tree with minimal height.
def binary_tree_from_sorted_list(sorted_list):
    # make middle root
    # split into L/R groups
    # make middle of L group root of new tree on left
    # make middle of R group root of new tree on right
    # continue
    pass


# 4.3 List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
def list_of_depths(binary_tree):
    # initial list - add root
    # add left and right to list?
    pass


# 4.4 Check Balanced: Implement a function to check if a binary tree is balanced.  For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.
def is_balanced(binary_tree):
    pass


# 4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.
def is_binary_search_tree(binary_tree):
    pass


# 4.6 Successor: Write an algorithm to find the "next" node (i.e., the in-order successor) of a given node in a
# binary search tree.  You may assume that each node has a link to its parent.

# 4.7 Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project).  ALl of a project's dependencies
# must be built before the project is.  Find a build order that will allow the projects to be built.  If there
# is no valid build order, return an error.

# 4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree.  Avoid storing additional nodes in a data structure.  NOTE: This is not
# necessarily a binary search tree.

# 4.9 BST Sequences: A binary search tree was created by traversing through an array from left to right
# and inserting each element.  Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.

# 4.10  Check Subtree; T1 and T2 are two very large binary trees, with T1 much bigger than T2.  Create an
# algorithm to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.

# 4.11 Random Node: You are implementing a binary tree class from scratch which, in addition to
# insert, find, and delete, has a method getRandomNode() which returns a random node
# from the tree.  ALl nodes should be equally likely to be chosen.  Design and implement an algorithm
# for getRandomNode, and explain how you would implement the rest of the methods.

# 4.12 Paths with Sum: You are given a binary tree in which each node contains an integer value (which
# might be a positive or negative).  Design an algorithm to count the number of paths that sum to a
# given value.  The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).

