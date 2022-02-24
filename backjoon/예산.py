N = int(input(''))
array = list(map(int,input().split(' ')))
M = int(input(''))

start ,end = 0, max(array)

while start <= end:
    mid = (start+end) // 2

    total = 0
    for money in array:
        total += min(mid,money)

    print(total, mid)
    if total > M:
        end = mid-1
    else:
        start = mid+1

if mid > M:
    print(mid-1)
else:
    print(mid)
