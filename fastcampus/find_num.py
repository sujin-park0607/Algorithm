from re import L


n = int(input(''))
num_list = list(map(int,input().split(' ')))

m = int(input(''))
find_num = list(map(int,input().split(' ')))


result = []
for i in find_num:
    if i in num_list:
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i)   

######특정 정수의 등장 여부만을 간단히  체크하면 됨
##### set을 이용해 간단해 풀 수 있음 -> 중복 허용 x 
###python에서는 dictionary자료형으로 사용하면 됨


n = int(input())
array = set(map(int,input().split()))

m = int(input())
x = list(map(int,input().split()))

for i in x:
    if i not in array:
        print('0')
    else:
        print('1')