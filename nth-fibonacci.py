results = {}

def getNthFib(n):
	fibs = [0]
	count = 1
	while count <= n:
		fibs.append(fib(count))
		count += 1
	return fibs[n-1]

def fib(n):
    if n >= 3:
        if n in results:
            return results[n]

        this_result = fib(n-1) + fib(n-2)
        results[n] = this_result
        return this_result
    else:
        return 1