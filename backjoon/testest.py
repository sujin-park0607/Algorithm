n = int(input())
n_array = list(map(int,input().split()))

count = {}

m = int(input())
card = list(map(int,input().split()))

for data in n_array:
    if data in count:
        count[data] += 1
    else:
        count[data] = 1

for target in card:
    if target not in count:
        print(0,end=' ')
    else:
        print(count[target], end=' ')
