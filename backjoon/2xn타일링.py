n = int(input())

d = [] * 1000


def dp(x):
    if(x==1): return 1
    if(x==1): return 2
    if d[x] != 0: return d[x]
    d[x] = dp(x-1)+dp(x-2) % 10007
    return d[x]