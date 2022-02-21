#내가푼 문제

list = input().split(" ")

#print(int(list))
up = 0
down = 0

for index in range (len(list)-1):
    if int(list[index]) < int(list[index+1]):
        up += 1
    elif int(list[index]) > int(list[index+1]):
        down += 1

if up == 7:
    print('ascending')
elif down == 7:
    print('descending')
else:
    print('mixed')

#다른풀이

#오름차순 True, 내림차순 True 초기상태
#오름차순 False ->ascending
#내림차순 False-> descending
#오름차선 False, 내림차순 False-> mix상태 

a = list(map(int, input().split(' ')))

ascending = True
descending = False

for index in range(1,8):
    if a[index] > a[index -1]:
        descending = False
    elif a[index] < a[index-1]:
        ascending = False
    
if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')