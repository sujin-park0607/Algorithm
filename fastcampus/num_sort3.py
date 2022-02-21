# n = int(input())
# array = []
# # result = []
# for _ in range(n):
#     num = int(input())
#     array.append(num)

# array.sort()
# # for i in range(0,10000,1):
# #     for j in array:
# #         if i==j:
# #             result.append(j)

# for i in array:
#     print(i)

##########계수정렬
#데이터가 등장한 횟수를 센다
#계수정렬

import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)