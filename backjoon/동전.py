N, total = map(int,input().split(' '))

coin = []
for _ in range(N):
    coin.append(int(input()))

coin = sorted(coin, reverse=True)


result = 0
i=0
while total:  
    if coin[i] <= total:
        cnt = total // coin[i]
        total -= cnt * coin[i]
        result += cnt
    i += 1

print(result)
        
