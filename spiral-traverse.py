"""
    Write a function that takes in an n x m two-dimensional array (that can be
    square-shaped when n == m) and returns a one-dimensional array of all the
    array's elements in spiral order.

    Spiral order starts at the top left corner of the two-dimensional array, goes
    to the right, and proceeds in a spiral pattern all the way until every element
    has been visited.

    Example:
        Input: 
            array = [
                [1, 2, 3, 4],
                [12, 13, 14, 5],
                [11, 16, 15, 6],
                [10, 9, 8, 7],
            ]
        Output:
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""
def spiralTraverse(array):
    results = []
    visited = [[False for row in array[0]] for col in array]
    traverse(array, visited, results, 0, 0, "right")
    return results

def traverse(matrix, visited, results, row, col, d):
    if visited[row][col] == False:
        results.append(matrix[row][col])
        visited[row][col] = True

    for neighbor in get_next(matrix, visited, row, col, d):
        i, j = neighbor
        traverse(matrix, visited, results, i, j, get_direction(i, row, j, col))

def get_next(matrix, visited, row, col, direction):
    if direction == "right":
        if is_valid(row, col+1, "col", visited):
            return [[row, col+1]]
        elif is_valid(row+1, col, "row", visited):
            return [[row+1, col]]
    elif direction == "down":
        if is_valid(row+1, col, "row", visited):
            return [[row+1, col]]
        elif is_valid(row, col-1, "col", visited):
            return [[row, col-1]]
    elif direction == "left":
        if is_valid(row, col-1, "col", visited):
            return [[row, col-1]]
        elif is_valid(row-1, col, "row", visited):
            return [[row-1, col]]
    elif direction == "up":
        if is_valid(row-1, col, "row", visited):
            return [[row-1, col]]
        elif is_valid(row, col+1, "col", visited):
            return [[row, col+1]]
    return []

def is_valid(row, col, change_type, visited):
    if change_type == "row":
        return row >= 0 and row <= len(visited) - 1 and visited[row][col] == False
    else:
        return col >= 0 and col <= len(visited[0]) - 1 and visited[row][col] == False

def get_direction(row, old_row, col, old_col):
    if row != old_row:
        d = "down" if row > old_row else "up"
    else:
        d = "right" if col > old_col else "left"
    return d