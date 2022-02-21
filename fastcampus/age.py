# n = int(input())
# list = []
# for i in range(n):
#     age, name = input().split()
#     list.append([int(age), name])

# list = list.sort()

# for i in list:
#     print(i[0],i[1])


##########
#튜플로 이용하여 데이터를 묶고 진행 

n = int(input())
array = []

for _ in range(n):
    input_data = input().split(' ')
    array.append((int(input_data[0]), input_data[1]))

array = sorted(array, key=lambda x:x[0])

for i in array:
    print(i[0],i[1])