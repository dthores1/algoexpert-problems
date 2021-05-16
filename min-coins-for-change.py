"""
    Given an array of positive integers representing coin denominations and a
    single non-negative integer n representing a target amount of
    money, write a function that returns the smallest number of coins needed to
    make change for (to sum up to) that target amount using the given coin
    denominations.

    Note that you have access to an unlimited amount of coins. In other words, if
    the denominations are [1, 5, 10], you have access to an unlimited
    amount of 1s, 5s, and 10s.

    If it's impossible to make change for the target amount, return -1.

    Example:
        n = 7
        denoms = [1, 5, 10]

        Output: 
            3
"""
def minNumberOfCoinsForChange(n, denoms):	
	min_coins = [float("inf") for amount in range(n+1)]
	min_coins[0] = 0
	
	for cents in range(n+1):		
		for c in [i for i in denoms if i <= cents]:
			min_coins[cents] = min(min_coins[cents - c] + 1, min_coins[cents])
				
	return min_coins[n] if min_coins[n] != float("inf") else -1

assert minNumberOfCoinsForChange(7, [1, 5, 10]) == 3
assert minNumberOfCoinsForChange(63, [1, 5, 10, 25]) == 6
assert minNumberOfCoinsForChange(63, [1, 5, 10, 21, 25]) == 3
assert minNumberOfCoinsForChange(7, [2, 4]) == -1
assert minNumberOfCoinsForChange(0, [1, 2, 3, 4, 5]) == 0