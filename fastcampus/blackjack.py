# num, max = map(int, input().split(' '))
# card = list(map(int, input().split(' ')))

# if len(card) != num:
#     print('error')

# result = 0
# for num1 in card:
#     for num2 in card:
#         for num3 in card:
#            total = num1 + num2 + num3
#            if total > result and total <= max :
#                result = total
#             # if total <= max:
#             #     result = max(result, total)

# print(max)

n, m = map(int, input().split(' '))
data = list(map(int, input().split(' ')))

result = 0
length = len(data)

count = 0
for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                result = max(result, sum_value)

print(result)
