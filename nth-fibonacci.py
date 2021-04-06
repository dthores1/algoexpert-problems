def getNthFib(n):
	fibs = [0]
	count = 1
	while count <= n:
		fibs.append(fib(count))
		count += 1
	return fibs[n-1]

def fib(n):
	if n >= 3:
		return fib(n-1) + fib(n-2)
	else:
		return 1