"""
    Write a function that takes in a non-empty array of integers that are sorted
    in ascending order and returns a new array of the same length with the squares
    of the original integers also sorted in ascending order.

    Example:
        array = [-10, -5, 0, 5, 10]

        Output:
            [0, 25, 25, 100, 100]
"""

def sortedSquaredArray(array):
    squares = []
    neg_squares_stack = []

    for i in array:
        sq = i*i
        if i >= 0:
            while len(neg_squares_stack) and sq > neg_squares_stack[-1]:
                squares.append(neg_squares_stack.pop())
            squares.append(sq)
        else:
            neg_squares_stack.append(sq)

    while len(neg_squares_stack):
        squares.append(neg_squares_stack.pop())

    return squares

print(sortedSquaredArray([-10, -5, 0, 5, 10]))