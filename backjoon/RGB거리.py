n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

for i in range(1,len(array)):
    for j in range(3):
        if array[i][j] == array[i][0]:
            array[i][j] += min(array[i-1][1],array[i-1][2])

        elif array[i][j] == array[i][1]:
            array[i][j] += min(array[i-1][0],array[i-1][2])

        else:
            array[i][j] += min(array[i-1][0],array[i-1][1])

print(min(array[-1]))