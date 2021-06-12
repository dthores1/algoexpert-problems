"""
    Write a function that takes in a potentially invalid Binary Search Tree (BST)
    and returns a boolean representing whether the BST is valid.

    Each BST node has an integer value, a
    left child node, and a right child node. A node is
    said to be a valid BST node if and only if it satisfies the BST
    property: its value is strictly greater than the values of every
    node to its left; its value is less than or equal to the values
    of every node to its right; and its children nodes are either valid
    BST nodes themselves or None / null.

    A BST is valid if and only if all of its nodes are valid
    BST nodes.

    Example:
tree =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14

    Output: true
"""
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
	return helper(tree, float("-inf"), float("inf"))

def helper(tree, min_value, max_value):
	if tree is None:
		return True
	if tree.value < min_value or tree.value >= max_value:
		return False
	left_is_valid = helper(tree.left, min_value, tree.value)
	return left_is_valid and helper(tree.right, tree.value, max_value)