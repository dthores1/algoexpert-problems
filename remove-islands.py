"""
    You're given a two-dimensional array (a matrix) of potentially unequal height
    and width containing only 0s and 1s. The matrix
    represents a two-toned image, where each 1 represents black and
    each 0 represents white. An island is defined as any number of
    1s that are horizontally or vertically adjacent (but not
    diagonally adjacent) and that don't touch the border of the image. In other
    words, a group of horizontally or vertically adjacent 1s isn't an
    island if any of those 1s are in the first row, last row, first
    column, or last column of the input matrix.

    Note that an island can twist. In other words, it doesn't have to be a
    straight vertical line or a straight horizontal line; it can be L-shaped, for
    example.

    You can think of islands as patches of black that don't touch the border of
    the two-toned image.

    Write a function that returns a modified version of the input matrix, where
    all of the islands are removed. You remove an island by replacing it with
    0s.

    Naturally, you're allowed to mutate the input matrix.

    Example:
        matrix = [
                    [1, 0, 0, 0, 0, 0],
                    [0, 1, 0, 1, 1, 1],
                    [0, 0, 1, 0, 1, 0],
                    [1, 1, 0, 0, 1, 0],
                    [1, 0, 1, 1, 0, 0],
                    [1, 0, 0, 0, 0, 1]
                ]

        Output:
            [
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1],
                [0, 0, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 0],
                [1, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 1]
            ] 
"""
def removeIslands(matrix):
    non_islands = get_non_islands(matrix)

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            if matrix[i][j] == 1 and non_islands[i][j] == False:
                matrix[i][j] = 0

    return matrix


def get_non_islands(matrix):
    non_islands = [[False for row in matrix[0]] for row in matrix]
    search_row(0, matrix, non_islands)
    search_row(len(matrix)-1, matrix, non_islands)
    search_col(0, matrix, non_islands)
    search_col(len(matrix[0])-1, matrix, non_islands)
    return non_islands

def search_row(row, matrix, non_islands):    
    for j in range(len(matrix[row])):
        search(row, j, matrix, non_islands)


def search(row, col, matrix, non_islands):
    if matrix[row][col] == 1:
        non_islands[row][col] = True

        for neighbor in get_neighbors(row, col, matrix, non_islands):
            this_row, this_col = neighbor
            search(this_row, this_col, matrix, non_islands)


def search_col(col, matrix, non_islands):
    for i in range(len(matrix)):
        search(i, col, matrix, non_islands)

def get_neighbors(i, j, matrix, non_islands):
    neighbors = []

    if i > 0 and matrix[i-1][j] == 1 and non_islands[i-1][j] == False:
        neighbors.append([i-1, j])
    if j > 0 and matrix[i][j-1] == 1 and non_islands[i][j-1] == False:
        neighbors.append([i, j-1])
    if i < len(matrix)-1 and matrix[i+1][j] == 1 and non_islands[i+1][j] == False:
        neighbors.append([i+1, j])
    if j < len(matrix[i])-1 and matrix[i][j+1] == 1 and non_islands[i][j+1] == False:
        neighbors.append([i, j+1])

    return neighbors


matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
]

print(removeIslands(matrix))