"""
    You're given a Node class that has a name and an array of optional children nodes. When put together, nodes
    form an acyclic tree-like structure. 

    Implement the breadthFirstSearch method on the Node class, which takes in an empty array, traverses the tree
    using the Breadth-first Search approach (specifically navigating the tree from left to right), stores all
    the nodes' names in the input array, and returns it. 
"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
		queue = [self]
		visited = set()
		
		while len(queue) > 0:
			node = queue.pop(0)
			array.append(node.name) # "Visit" the node
			
			for i in node.children:
				if i.name not in visited:
					visited.add(i.name)
					queue.append(i)
		
		return array