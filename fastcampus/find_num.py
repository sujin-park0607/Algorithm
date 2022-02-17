n = int(input(''))
num_list = list(map(int,input().split(' ')))

m = int(input(''))
find_num = list(map(int,input().split(' ')))

if n != len(num_list) or m != len(find_num):
    print('error')

result = []
for i in find_num:
    if i in num_list:
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i)   