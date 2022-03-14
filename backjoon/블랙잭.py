n, m = map(int, input().split())
array = list(map(int,input().split()))

result = 0

for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        for k in range(j+1,len(array)):
            sum_value = array[i] + array[j] + array[k]

            if sum_value <= m:
                result = max(result,sum_value)

print(result)
