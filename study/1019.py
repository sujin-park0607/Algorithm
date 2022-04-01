num_array = [0] * 10

n = int(input())
for i in range(1,n+1):
    num = list(str(i))
    for j in num:
        num_array[int(j)] += 1
result = " ".join(map(str, num_array))
print(result)

