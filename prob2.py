num = int(input('Enter a number :'))

for i in range(num+1):
	for j in range(i):
		print(j+1, end=" ")
	print()
