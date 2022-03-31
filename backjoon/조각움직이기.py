from itertools import combinations,permutations
from collections import deque
dR=[0,0,-1,1]
dC=[1,-1,0,0]
INF=9876543210

def calDist(A,B):
    return abs(A[0]-B[0])+abs(A[1]-B[1])

def isConnect(nowL):
    visited=[[0 for j in range(5)] for i in range(5)]
    tempL=[[0 for j in range(5)] for i in range(5)]
    for r,c in nowL:
        tempL[r][c]=1
    visited[nowL[0][0]][nowL[0][1]]=1
    cntCon=1
    q=deque([[nowL[0][0],nowL[0][1]]])
    while(q):
        r,c=q.popleft()
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<5 and 0<=tempC<5 and visited[tempR][tempC]==0 and tempL[tempR][tempC]==1:
                visited[tempR][tempC]=1
                q.append([tempR,tempC])
                cntCon+=1
    if cntCon==size:
        return True
    else:
        return False

L=[]
for i in range(5):
    L.append(list(input()))
loc=[]
for i in range(5):
    for j in range(5):
        if L[i][j]=="*":
            loc.append([i,j])
size=len(loc)


comb=list(combinations([i for i in range(25)],size))
ans=INF
for numL in comb:
    # 번호->행렬
    nowLoc=[]
    for i in numL:
        r=i//5
        c=i%5
        nowLoc.append([r,c])

    # 연결여부확인
    if not isConnect(nowLoc):
        continue

    # 거리확인
    nowAns=INF
    per=list(permutations([i for i in range(size)],size))
    for myTuple in per:
        temp=0
        for i in range(size):
            temp+=calDist(loc[i],nowLoc[myTuple[i]])
        if temp<nowAns:
            nowAns=temp

    if nowAns<ans:
        ans=nowAns

print(ans)
