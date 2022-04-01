n = int(input())
array = []
for _ in range(n):
    n, m = map(int,input().split())
    array.append((n,m))

array = sorted(array, key = lambda x: (x[0],x[1]))

for i in array:
    print(i[0],i[1])

