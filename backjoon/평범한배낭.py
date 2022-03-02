n, k = map(int,input().split())

array = [[0] * (k+1) for _ in range (n+1)]

for i in range(1,n+1):
    weight, value = map(int,input().split())
    for j in range(1,k+1):
        if weight > j:
            array[i][j] = array[i-1][j]
        else:
            array[i][j] = max(array[i-1][j], array[i-1][j-weight] + value)

print(array[n][k]) 