str1 = 'Abc'
str2 = 'Xyz'

str3 = []

j=len(str2)-1
for i in range(len(str1)):
	str3.append(str1[i])
	str3.append(str2[j])
	j-=1
	
str3 = ''.join(str3)
print(str3)
