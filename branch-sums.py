"""
    Write a function that takes in a Binary Tree and returns a list of its branch
    sums ordered from leftmost branch sum to rightmost branch sum.

    A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree
    branch is a path of nodes in a tree that starts at the root node and ends at
    any leaf node.
"""
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
	results = []
	sum_branches(root, 0, results)
	return results
	
# Using pre-order traversal
def sum_branches(node, current_sum, results=[]):
	current_sum += node.value
	
	if node.left is None and node.right is None:
		results.append(current_sum)	
	
	if node.left:
		sum_branches(node.left, current_sum, results)
	
	if node.right:
		sum_branches(node.right, current_sum, results)	