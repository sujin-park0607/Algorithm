n = int(input())

cnt = 0
while n > 1:
    if n>=3:
        if n%3 == 1:
            n -= 1
            n = n // 3
            cnt += 2
        else:
            n = n // 3
            cnt += 1

    elif n>=2:
        if n%2 == 1:
            n-= 1
            n = n// 2
            cnt += 2
        else:
            n = n// 2
            cnt += 1    
    else:
        n -= 1
        cnt += 1
print(cnt)