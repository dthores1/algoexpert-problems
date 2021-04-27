"""
    You're given a two-dimensional array (a matrix) of potentially unequal height
    and width containing only 0s and 1s. Each
    0 represents land, and each 1 represents part of a
    river. A river consists of any number of 1s that are either
    horizontally or vertically adjacent (but not diagonally adjacent). The number
    of adjacent 1s forming a river determine its size.

    Note that a river can twist. In other words, it doesn't have to be a straight
    vertical line or a straight horizontal line; it can be L-shaped, for example.

    Write a function that returns an array of the sizes of all rivers represented
    in the input matrix. The sizes don't need to be in any particular order.

    Example:
        matrix = [
                    [1, 0, 0, 1, 0],
                    [1, 0, 1, 0, 0],
                    [0, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 0],
                ]

        Output: [1, 2, 2, 2, 5] // The numbers could be ordered differently.

"""

def riverSizes(matrix):
    results = []
    visited = [[False for i in matrix[0]] for col in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            
            if matrix[i][j] == 1:
                traverse(i, j, matrix, 0, visited, results)

    return results

def traverse(i, j, matrix, curr_size, visited, results):  
    stack = [[i, j]]

    while len(stack):
        node = stack.pop()
        row, col = node

        if not visited[row][col] and matrix[row][col] == 1:
            curr_size += 1
        visited[row][col] = True

        if matrix[row][col] == 1:
            for x in get_neighbors(row, col, matrix, visited):
                stack.append(x)

    results.append(curr_size)

def get_neighbors(i, j, matrix, visited):
    neighbors = []

    if i > 0 and not visited[i-1][j]:
        neighbors.append([i-1, j])
    if i+1 < len(matrix) and not visited[i+1][j]:
        neighbors.append([i+1, j])
    if j > 0 and not visited[i][j-1]:
        neighbors.append([i, j-1])
    if j+1 < len(matrix[i]) and not visited[i][j+1]:
        neighbors.append([i, j+1])

    return neighbors