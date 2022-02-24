#딕셔너리 사용
n = int(input())
n_data = list(map(int,input().split(' ')))

m = int(input())
m_list = list(map(int,input().split(' ')))

count = {}

for data in n_data:
    if data in count:
        count[data] += 1
    else:
        count[data] = 1

for target in m_list:
    result = count.get(target)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")

#이분탐색 사용

# import sys
# input = sys.stdin.readline

# n = int(input())
# n_data = sorted([*map(int,input().split())])

# m = int(input())
# m_array = [*map(int,input().split())]

# count = {}
# for data in n_data:
#     if data in count:
#         count[data] += 1
#     else:
#         count[data] = 1

# print(count)

# def binary_search(arr, value, start, end):
#     if start > end:
#         return 0
    
#     mid = (start+end) //2
#     if arr[mid] == value:
#         return count.get(value)
#     elif arr[mid] > value:
#         return binary_search(arr, target, start,mid-1)
#     else:
#         return binary_search(arr,target,mid+1,end)

# for target in m_array:
#     print(binary_search(n_data, target, 0, len(n_data)-1),end =" ")
