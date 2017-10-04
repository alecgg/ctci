from collections import deque
from itertools import permutations
from random import choice


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
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = None

    def __len__(self):
        size = 1
        if self.left is not None:
            size += len(self.left)
        if self.right is not None:
            size += len(self.right)
        return size

    def height(self):
        left_height = self.left.height() if self.left is not None else 0
        right_height = self.right.height() if self.right is not None else 0
        return 1 + max([left_height, right_height])

    def max_child(self):
        left_max = self.left.max_child() if self.left is not None else None
        right_max = self.right.max_child() if self.right is not None else None
        if left_max is None and right_max is None:
            return None
        return max(n for n in [left_max, right_max] if n is not None)

    def min_child(self):
        left_min = self.left.min_child() if self.left is not None else None
        right_min = self.right.min_child() if self.right is not None else None
        if left_min is None and right_min is None:
            return None
        return min(n for n in [left_min, right_min] if n is not None)

    def is_binary_search_tree_root(self):
        max_left = self.left.max_child() if self.left is not None else None
        min_right = self.right.min_child() if self.right is not None else None
        if max_left is None and min_right is None:
            return True
        elif max_left is None:
            return max_left <= self.value
        elif min_right is None:
            return self.value < min_right
        return max_left <= self.value < min_right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __len__(self):
        return len(self.root)

    def height(self):
        return self.root.height()

    def is_binary_search_tree(self):
        return self.root.is_binary_search_tree_root()


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
    if len(sorted_list) == 0:
        return BinaryTree()
    if len(sorted_list) == 1:
        root = TreeNode(value=sorted_list[0])
        return BinaryTree(root=root)
    mid = len(sorted_list) // 2
    root = TreeNode(sorted_list[mid])
    tree = BinaryTree(root=root)
    root.right = binary_tree_from_sorted_list_helper(sorted_list, mid + 1, len(sorted_list) - 1)
    root.left = binary_tree_from_sorted_list_helper(sorted_list, 0, mid - 1)
    return tree


def binary_tree_from_sorted_list_helper(sorted_list, i, j):
    if i > j:
        return None
    if i == j:
        return TreeNode(value=sorted_list[i])
    mid = (i + j) // 2
    root = TreeNode(sorted_list[mid])
    root.right = binary_tree_from_sorted_list_helper(sorted_list, mid + 1, j)
    root.left = binary_tree_from_sorted_list_helper(sorted_list, i, mid - 1)
    return root


# 4.3 List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
def list_of_depths(binary_tree: BinaryTree) -> bool:
    if binary_tree.root is None:
        return []

    root = binary_tree.root
    linked_lists = deque([root])
    depth_queue = deque([root])
    while len(depth_queue) > 0:
        linked_list = depth_queue.popleft()
        next_linked_list = deque()
        for node in linked_list:
            if node.left is not None:
                next_linked_list.append(node.left)
            if node.right is not None:
                next_linked_list.append(node.right)
        depth_queue.append(next_linked_list)
        linked_lists.append(next_linked_list)
    return linked_lists


# 4.4 Check Balanced: Implement a function to check if a binary tree is balanced.  For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.
def is_balanced(binary_tree: BinaryTree) -> bool:
    # just need height, not size
    nodes_to_visit = deque([binary_tree.root])
    while nodes_to_visit is not None:
        node = nodes_to_visit.popleft()
        left_height = node.left.height() if node.left is not None else 0
        right_height = node.right.height() if node.right is not None else 0
        if abs(left_height - right_height) > 1:
            return False
        nodes_to_visit.extend(n for n in [node.left, node.right] if n is not None)
    return True


# 4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.
def is_binary_search_tree(binary_tree: BinaryTree) -> bool:
    # need to validate all on left <= me < right
    # so get max value from left
    # and min value from right
    # compare to me
    return binary_tree.is_binary_search_tree()


# 4.6 Successor: Write an algorithm to find the "next" node (i.e., the in-order successor) of a given node in a
# binary search tree.  You may assume that each node has a link to its parent.
def successor(node: TreeNode) -> TreeNode:
    # if you have a right child, then it's the left-most child on the right-side (smallest thing greater than you)
    # if you have no right child, then it's the earliest parent that is greater than you
    # you are the end of a in-order traversal of a left-subtree
    # so go back up to the node who's left-side has been explored
    if node.right is None:
        parent = node.parent
        while parent is not None:
            if node.value <= parent.value:
                return parent
            parent = parent.parent
        return parent
    child = node.right
    while child.left is not None:
        child = child.left
    return child


# 4.7 Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project).  ALl of a project's dependencies
# must be built before the project is.  Find a build order that will allow the projects to be built.  If there
# is no valid build order, return an error.
def build_order(projects, dependencies):
    # find projects with no dependencies
    # add projects to initial list
    # remove dependencies on those projects
    # find projects with no dependencies...
    # repeat...
    projects = projects[:]
    dependencies = dependencies[:]

    dependees = [d[1] for d in dependencies]
    no_dependencies_projects = [p for p in projects if p not in dependees]
    if len(no_dependencies_projects) == 0:
        return 'ERROR'

    build = no_dependencies_projects[:]
    while len(no_dependencies_projects) > 0:
        projects = [p for p in projects if p not in build]
        dependencies = [d for d in dependencies if d[0] not in build]
        dependees = [d[1]for d in dependencies]
        no_dependencies_projects = [p for p in projects if p not in dependees]
        build = [p for p in no_dependencies_projects if p not in build]

    if len(projects) != 0:
        return 'ERROR'
    return build


# 4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree.  Avoid storing additional nodes in a data structure.  NOTE: This is not
# necessarily a binary search tree.
def first_common_ancestor(node, other_node):
    # do like a nested for loop.  start at node and other node
    # check if going up other node's ancestors meets node
    # if not, update node to node.parent and try again
    ancestor = node
    while ancestor is not None:
        check_node = other_node
        while check_node is not None:
            if ancestor is check_node:
                return ancestor
            check_node = check_node.parent
        ancestor = ancestor.parent
    return ancestor


# 4.9 BST Sequences: A binary search tree was created by traversing through an array from left to right
# and inserting each element.  Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.
def bst_sequences(binary_search_tree):
    # make array out of BST
    # generate all permutations of array
    array = []
    to_visit = deque([binary_search_tree.root])
    while len(to_visit) > 0:
        node = to_visit.popleft()
        if node is None:
            continue
        array.append(node.value)
        to_visit.extend([node.left, node.right])
    return permutations(array)


# 4.10  Check Subtree; T1 and T2 are two very large binary trees, with T1 much bigger than T2.  Create an
# algorithm to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.
def is_subtree(bigger_tree, smaller_tree):
    # look for the root of the smaller tree in the bigger tree
    # could get height of smaller tree and not go deeper than that into larger tree
    nodes_to_search = deque(bigger_tree.root)
    while len(nodes_to_search) > 0:
        node = nodes_to_search.popleft()
        if node is smaller_tree.root:
            return node
        if node is None:
            continue
        nodes_to_search.extend([node.left, node.right])
    return None


# 4.11 Random Node: You are implementing a binary tree class from scratch which, in addition to
# insert, find, and delete, has a method getRandomNode() which returns a random node
# from the tree.  ALl nodes should be equally likely to be chosen.  Design and implement an algorithm
# for getRandomNode, and explain how you would implement the rest of the methods
def get_random_node(binary_tree):
    # flatten array into an array and pick random element
    # pointer to root
    nodes_to_search = deque([binary_tree.root])
    nodes = []
    while len(nodes_to_search) > 0:
        node = nodes_to_search.popleft()
        if node is None:
            continue
        nodes.append(node)
        nodes_to_search.extend([node.left, node.right])
    return choice(nodes)


# 4.12 Paths with Sum: You are given a binary tree in which each node contains an integer value (which
# might be a positive or negative).  Design an algorithm to count the number of paths that sum to a
# given value.  The path does not need to start or end at the root or a leaf, but it must go downwards
# (traveling only from parent nodes to child nodes).
def path_sum(binary_tree, value):
    # each node has a sum value, do an in-order traversal
    nodes_to_search = deque([(binary_tree.root, binary_tree.root.value)])
    paths = 0
    while len(nodes_to_search) > 0:
        node, node_sum = nodes_to_search.popleft()
        if node_sum == value:
            paths += 1
        nodes_to_search.extend([
            (n, n.value + node_sum) for n in [node.left, node.right] if n is not None
        ])
    return paths