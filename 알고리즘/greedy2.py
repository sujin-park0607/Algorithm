n = int(input())

data_list = list(map(int, input().split(' ')))

data_list.sort()
result = 0

for i in range(len(data_list)):
    result += sum(data_list[:i+1])

