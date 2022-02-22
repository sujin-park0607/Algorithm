# n = int(input())
# A = list(map(int,input().split(' ')))

# m = int(input())
# array = list(map(int,input().split(' ')))

# for num in array:
#     if num in A:
#          print(1)
#     else:
#         print(0)



def binary_search(A, search_data):
    if len(A) == 1 and A[0] == search_data:
        return True
    if len(A) == 1 and A[0] != search_data:
        return False
    if len(A) == 0:
        return False
    med = len(A) // 2
    if A[med] == search_data:
        return True
    else:
        if A[med] < search_data:
            return binary_search(A[med:],search_data)
        elif A[med] > search_data:
            return binary_search(A[:med],search_data)

A = [4,1,2,3,5]
A.sort()
search_data = [1,3,7,9,5]

for i in range(len(search_data)):
    if binary_search(A,search_data[i]):
        print(1)
    else: print(0)





