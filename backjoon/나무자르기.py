import sys
N, M = map(int,sys.stdin.readline().split(' '))

array = list(map(int,sys.stdin.readline().split(' ')))
start = 1
end = max(array)

while start >= end:
    total = 0
    mid = (start+end) // 2

    for m in array:
        total += (m - mid)
    print(total)
    if total <= M:
        end = mid -1
        
    else:
        start = mid + 1

print(end)

