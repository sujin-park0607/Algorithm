N = int(input())

array = list(map(int,input().split()))

array.sort()
r = []
result = 0
for i in range(N):
    result += array[i]
    r.append(result)

print(sum(r))
