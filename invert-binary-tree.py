"""
    Write a function that takes in a Binary Tree and inverts it. In other words, the function should swap
    every left node in the tree for its corresponding right node. 

    Each BinaryTree node has an integeger value, a left child node, and a right child node. Children nodes
    can either be BinaryTree nodes themselves or None/null.
"""

# O(n) time | O(d) space - d is the height of the binary tree
def invertBinaryTree(tree):
	tree.left, tree.right = tree.right, tree.left
	
	if tree.left:
		invertBinaryTree(tree.left)
		
	if tree.right:
		invertBinaryTree(tree.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None