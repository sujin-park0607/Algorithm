n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort()
print(array)

avg = sum(array) // 2 
w = max(min(array),avg)

print(w)