n = int(input())

array = []

for _ in range(n):
    array.append(int(input()))

sort_array = sorted(array,reverse=True)


result = 0
for a in range(n):
    i = array.index(sort_array[a])

    if i==0 or array[i+1]=='o' and array[i+2] == 'o':
        print(i)
        continue
        
    elif i == (n-1) or array[i-1]=='o' and array[i-2] == 'o':
        print(i)
        continue

    else:
        print(i)
        if array[i-1] == 'o' and array[i+1] == 'o':
            continue
        else:
            result += array[i]
            array[i] = 'o'

    

print(result)

