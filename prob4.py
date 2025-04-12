str1 = 'P@#yn26at^&i5ve'

lowercase = 0
uppercase = 0
number = 0
symbol = 0

for i in range(len(str1)):
	if str1[i].islower():
		lowercase+=1
	
	elif str1[i].isupper():
		uppercase+=1
	
	elif str1[i].isnumeric():
		number+=1
	
	else:
		symbol+=1

print(f'lowrcase = {lowercase}')
print(f'uppercase = {uppercase}')
print(f'number = {number}')
print(f'symbol = {symbol}')
