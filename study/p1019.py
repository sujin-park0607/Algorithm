<<<<<<< HEAD:study/p1019.py
num_array = [0] * 10

n = int(input())
for i in range(1,n+1):
    num = list(str(i))
    for j in num:
        num_array[int(j)] += 1
result = " ".join(map(str, num_array))
print(result)

=======
#sample data
# num_array = [0] * 10
# n = int(input())
# for i in range(1,n+1):
#     num = list(str(i))
#     for j in num:
#         num_array[int(j)] += 1
# result = " ".join(map(str, num_array))
# print(result)


n = int(input())
s = [0 for i in range(10)]
point = 1
while n != 0:
    while n % 10 != 9:
        for i in str(n):
            s[int(i)] += point
        n -= 1
    if n < 10:
        for i in range(n + 1):
            s[i] += point
        s[0] -= point
        break
    else:
        for i in range(10):
            s[i] += (n // 10 + 1) * point
    s[0] -= point
    point *= 10
    n //= 10
for i in s:
    print(i, end=' ')
>>>>>>> 35320871bad1f5a99eba81740d26e4c79e5cce88:study/1019.py
