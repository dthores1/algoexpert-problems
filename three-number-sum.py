"""
    Write a function that takes in a non-empty array of distinct integers and an
    integer representing a target sum. The function should find all triplets in
    the array that sum up to the target sum and return a two-dimensional array of
    all these triplets. The numbers in each triplet should be ordered in ascending
    order, and the triplets themselves should be ordered in ascending order with
    respect to the numbers they hold.


    If no three numbers sum up to the target sum, the function should return an
    empty array.   

    Example:
        array = [12, 3, 1, 2, -6, 5, -8, 6]
        targetSum = 0

        Output:
            [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]] 
"""
def threeNumberSum(array, targetSum):
    results = []
    array.sort()

    for index in range(len(array) - 2):
        num1 = array[index]

        second_index = index + 1
        last_index = len(array) - 1

        while second_index < last_index:
            res = num1 + array[second_index] + array[last_index]

            if res == targetSum:
                results.append([num1, array[second_index], array[last_index]])
                second_index += 1
                last_index -= 1
            elif res < targetSum:
                second_index += 1
            elif res > targetSum:
                last_index -= 1

    return results