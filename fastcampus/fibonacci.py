n = int(input())

a = 0
b = 1
count = 1

while count < n:
    a , b = b, a+b
    count += 1
    
print(b)
    