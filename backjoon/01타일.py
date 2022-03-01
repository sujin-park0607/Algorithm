n = int(input())

array = [0] * 1000001
array[1] = 1
array[2] = 2

for i in range(3,n+1):
    array[i] = (array[i-1] + array[i-2])%15746

print(array[n])
    