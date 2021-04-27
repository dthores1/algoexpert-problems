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