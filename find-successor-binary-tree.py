"""
    Write a function that takes in a Binary Tree (where nodes have an additional
    pointer to their parent node) as well as a node contained in that tree and
    returns the given node's successor.

    A node's successor is the next node to be visited (immediately after the given
    node) when traversing its tree using the in-order tree-traversal technique. A
    node has no successor if it's the last node to be visited in the in-order
    traversal.

    If a node has no successor, your function should return None / null.

    Each BinaryTree node has an integer value, a
    parent node, a left child node, and a
    right child node. Children nodes can either be
    BinaryTree nodes themselves or None /
    null.
"""

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
	results = [] # In-order traversal list
	traverse_in_order(tree, results)
	
	# Find the current element in the list; we'll need to return the next index from that
	for i in range(len(results)):		
		if results[i].value == node.value and i+1 < len(results):	
			return results[i+1]
		
	return None
	
def traverse_in_order(node, results):
	if node.left:
		traverse_in_order(node.left, results)
		
	results.append(node)
		
	if node.right:
		traverse_in_order(node.right, results)		