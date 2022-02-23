n = int(input())
array = []
for _ in range(n):
    T, S = map(int,input().split(' '))
    array.append((T,S))
count = 1
for i in range(len(array)+1):
    if array[i][1] <= array[i+1][0]:
        count +=1
    else: count += 0

print(count) 