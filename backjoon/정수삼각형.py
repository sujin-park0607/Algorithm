n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

for i in range(1,len(array)):
    for j in range(len(array[i])):
        if j==0:
            # print(array[i][j],'-----1')
            array[i][j] += array[i-1][0]
        
        elif j==len(array[i])-1:
            array[i][j] += array[i-1][-1]
        else:
            array[i][j] += max(array[i-1][j-1], array[i-1][j])
            

print(max(array[-1]))
