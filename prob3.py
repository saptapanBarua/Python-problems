first = 0
second = 1
fibo = 0
for i in range(10):
	print(fibo, end=" ")
	fibo = first+second
	second=first
	first=fibo
