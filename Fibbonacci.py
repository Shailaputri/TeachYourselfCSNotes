#Fibonacci using Dynamic programming vs Recursion
'''
Implementing SICP concept of Recursion
'''
def fib_recur (n):
	#Base Case
	#When base case is reached, function returns its value to the function that had called it and memory is de-allocated
	if n<=1:
		#print("Yay")
		return n
	else:
		#print("Nay")
		return (fib_recur(n-1)+fib_recur(n-2))


for i in range (10):
	print(fib_recur(i))


def fib_DP (n):
	f = [0,1]
	i=2
	while i <= n:
		f.append(f[i-1]+f[i-2])
		i += 1
	return f[n]

print("New")
for i in range (10):
	print(fib_DP(i))
