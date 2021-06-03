"""
    Write a function that takes in an integer matrix of potentially unequal height
    and width and returns the minimum number of passes required to convert all
    negative integers in the matrix to positive integers.

    A negative integer in the matrix can only be converted to a positive integer
    if one or more of its adjacent elements is positive. An adjacent element is an
    element that is to the left, to the right, above, or below the current element
    in the matrix. Converting a negative to a positive simply involves multiplying
    it by -1.

    Note that the 0 value is neither positive nor negative, meaning
    that a 0 can't convert an adjacent negative to a positive.

    A single pass through the matrix involves converting all the negative integers
    that can be converted at a particular point in time. For example,
    consider the following input matrix:

        [ 
            [0, -2, -1], 
            [-5, 2, 0], 
            [-6, -2, 0]
        ]

    After a first pass, only 3 values can be converted to positives:

        [ 
            [0, 2, -1], 
            [5, 2, 0], 
            [-6, 2, 0]
        ]


  After a second pass, the remaining negative values can all be converted to
  positives:

        [ 
            [0, 2, 1], 
            [5, 2, 0], 
            [6, 2, 0]
        ]


    Note that the input matrix will always contain at least one element. If the
    negative integers in the input matrix can't all be converted to positives,
    regardless of how many passes are run, your function should return
    -1.

    Example:
        matrix = [
            [0, -1, -3, 2, 0],
            [1, -2, -5, -1, -3],
            [3, 0, 0, -4, -1],
        ]

        Output: 3
</div>
"""
def minimumPassesOfMatrix(matrix):
    passes = 0
    contains_negs = get_contains_negs(matrix)
    changes_made = 0

    if contains_negs == False:
        return passes

    while contains_negs:
        swapped_status = [[False for row in matrix[0]] for row in matrix]
        passes += 1
        changes_made = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] >= 0:
                    continue
                
                neighbors = get_neighbors(i, j, matrix, swapped_status)

                if len(neighbors) and max(neighbors) > 0:
                    swapped_status[i][j] = True
                    matrix[i][j] = abs(matrix[i][j])
                    changes_made += 1

        if changes_made == 0:
            return -1

        contains_negs = get_contains_negs(matrix)

    return passes

def get_contains_negs(matrix):
    for i in range(len(matrix)):
        if min(matrix[i]) < 0:
            return True

    return False

def get_neighbors(i, j, matrix, used):
    neighbors = []

    if i > 0 and used[i-1][j] == False:
        neighbors.append(matrix[i-1][j])
    if i < len(matrix) - 1 and used[i+1][j] == False:
        neighbors.append(matrix[i+1][j])
    if j > 0 and used[i][j-1] == False:
        neighbors.append(matrix[i][j-1])
    if j < len(matrix[i]) - 1 and used[i][j+1] == False:
        neighbors.append(matrix[i][j+1])
    
    return neighbors


matrix1 = [
    [0, -1, -3, 2, 0],
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1]
]

assert minimumPassesOfMatrix(matrix1) == 3

matrix2 =  [
    [1]
]

assert minimumPassesOfMatrix(matrix2) == 0

matrix3 =  [
    [1, 0, 0, -2, -3],
    [-4, -5, -6, -2, -1],
    [0, 0, 0, 0, -1],
    [1, 2, 3, 0, -2]
]

assert minimumPassesOfMatrix(matrix3) == 7

matrix4 = [
    [1, 0, 0, -2, -3],
    [-4, -5, -6, -2, -1],
    [0, 0, 0, 0, -1],
    [1, 2, 3, 0, 3]
]

assert minimumPassesOfMatrix(matrix4) == 4

matrix5 =  [
    [1, 0, 0, -2, -3],
    [-4, -5, -6, -2, -1],
    [0, 0, 0, 0, -1],
    [-1, 0, 3, 0, 3]
]

assert minimumPassesOfMatrix(matrix5) == -1