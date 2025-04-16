n = 121
n1 = n
n2 = 0

while (n1 > 0):
    n2 = (n2*10) + (n1%10)
    n1 //= 10
    
print(True)if(n==n2)else print(False)
