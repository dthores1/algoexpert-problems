"""
    You're given three inputs, all of which are instances of an
    AncestralTree class that have an ancestor property
    pointing to their youngest ancestor. The first input is the top ancestor in an
    ancestral tree (i.e., the only instance that has no ancestor--its
    ancestor property points to None / null), and the other two inputs are descendants 
    in the ancestral tree.

    Write a function that returns the youngest common ancestor to the two
    descendants.

    Note that a descendant is considered its own ancestor. So in the simple
    ancestral tree below, the youngest common ancestor to nodes A and B is node A.

    // The youngest common ancestor to nodes A and B is node A.
      A
     /
    B

    Example:
        # The nodes are from the ancestral tree below.
        topAncestor = node A
        descendantOne = node E
        descendantTwo = node I
          A
       /     \
      B       C
    /   \   /   \
   D     E F     G
 /   \
H     I

        Output: Node B
"""
# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	ancestors1 = get_ancestors(descendantOne)
	ancestors2 = get_ancestors(descendantTwo)
	
	# Go through the shallower list, returning the first element in the deeper list
	if len(ancestors1) > len(ancestors2):
		for a in ancestors2:
			if a in ancestors1:
				return a
	else:
		for b in ancestors1:
			if b in ancestors2:
				return b
			
	return None
	

def get_ancestors(descendant):
	ancestors = []
	
	curr_node = descendant
	while curr_node is not None:
		ancestors.append(curr_node)
		curr_node = curr_node.ancestor
		
	return ancestors
