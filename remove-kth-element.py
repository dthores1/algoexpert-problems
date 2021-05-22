"""
    Write a function that takes in the head of a Singly Linked List and an integer
    kand removes the kth node from the end of the list.


    The removal should be done in place, meaning that the original data structure
    should be mutated (no new structure should be created).


    Furthermore, the input head of the linked list should remain the head of the
    linked list after the removal is done, even if the head is the node that's
    supposed to be removed. In other words, if the head is the node that's
    supposed to be removed, your function should simply mutate its
    valueand nextpointer.

    Note that your function doesn't need to return anything.

    You can assume that the input Linked List will always have at least two nodes
    and, more specifically, at least k nodes.

    Each LinkedListnode has an integer valueas well as
    a nextnode pointing to the next node in the list or to
    None/ nullif it's the tail of the list.

    Example:
        head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 // the head node with value 0
        k = 4

        Output:
            // No output required.
            // The 4th node from the end of the list (the node with value 6) is removed.
            0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9
"""
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
	lead_pointer = head
	
	for i in range(k):
		lead_pointer = lead_pointer.next
	
	pointer_to_change = None
	second_pointer = head
	while lead_pointer is not None:
		lead_pointer = lead_pointer.next
		pointer_to_change = second_pointer
		second_pointer = second_pointer.next
		
	if pointer_to_change is not None:
		pointer_to_change.next = second_pointer.next
	else:
		second_pointer = head.next
		head.value, head.next = second_pointer.value, second_pointer.next
	