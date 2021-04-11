""" 
    Write a function that takes in an array of integers and returns the length of
    the longest peak in the array.

    A peak is defined as adjacent integers in the array that are strictly increasing 
    until they reach a tip (the highest value in the peak), at which point they become
    strictly decreasing. At least three integers are required to form a peak.

    Example:
        array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

        Output:
            6 # 0, 10, 6, 5, -1, -3
"""
def longestPeak(array):
    if len(array) <= 2:
        return 0

    longest_peak = 0
    peak_start = 0
    previous_directions = []
    increased = False

    # Add the direction that we're heading initially
    if array[1] > array[0]:
        previous_directions.append("increasing")
    elif array[1] < array[0]:
        previous_directions.append("decreasing")
    else:
        previous_directions.append("equals")

    for i in range(1, len(array)):
        if array[i] == array[i-1]:
            dir = "equals"
        else:
            dir = "increasing" if array[i] > array[i-1] else "decreasing"

        if dir == "increasing":
            increased = True
        
        if dir == "increasing" and previous_directions[-1] != "increasing":
            if increased and i - peak_start >= 3 and i - peak_start > longest_peak:
                longest_peak = i - peak_start             
            peak_start = i-1
        elif not increased:
            peak_start = i
        elif dir == "equals":
            if previous_directions[-1] != "decreasing":
                increased = False
                peak_start = i
            elif increased:
                if increased and i - peak_start >= 3 and i - peak_start > longest_peak:
                    longest_peak = i - peak_start
                peak_start = i

        previous_directions.append(dir)

    if previous_directions[-1] == "decreasing" and len(array) - peak_start >= 3 and len(array) - peak_start > longest_peak:
        longest_peak = len(array)  - peak_start 

    return longest_peak