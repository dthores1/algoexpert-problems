"""
    Write a function that takes in a non-empty array of integers and returns the
    maximum sum that can be obtained by summing up all of the integers in a
    non-empty subarray of the input array. A subarray must only contain adjacent
    numbers (numbers next to each other in the input array).

    Example:
        array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

        Output: 19
"""
import unittest

def kadanes(array):
    curr_total, max_sum = array[0], array[0]

    for i in range(1, len(array)):
        curr_total = max(curr_total + array[i], array[i])
        max_sum = max(curr_total, max_sum)
    
    return max_sum

class TestKadanes(unittest.TestCase):
    def test_1_simple(self):
        self.assertEqual(kadanes([-1, 1, 2, 3, -2]), 6)

    def test_2_negative_elements(self):
        self.assertEqual(kadanes([-1, 1, 2, 3, -2, 3]), 7)

    def test_3_local_optimum(self):
        self.assertEqual(kadanes([-1, 1, 2, -9, 4, -1]), 4)
        self.assertEqual(kadanes([-1, 4, -9, 1, 2, -1]), 4)

    def test_4_all_positive_elements(self):
        self.assertEqual(kadanes([1, 2, 3, 4, 5]), 15)

    def test_5_all_negative_elements(self):
        self.assertEqual(kadanes([-3, -6, -4, -1, -4, -15, -7]), -1)

if __name__ == "__main__":
    unittest.main()