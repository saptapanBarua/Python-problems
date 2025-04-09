str1 = input('Enter a string :')
str2 = []

for ch in str1:
	if ch.isupper():
		str2.append(chr(ord(ch) + 32))
				
	elif ch.islower():
		str2.append(chr(ord(ch) - 32))
		
	else:
		str2.append(ch)
		
str2 = ''.join(str2)
print(str2)
