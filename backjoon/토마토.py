from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int,input().split())
array = []
for _ in range(N):
    array.append(list(map(int,input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()
res = 0

for a in range(N):
    for b in range(M):
        if array[a][b] == 1:
            q.append((a,b))

def bfs(array):
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx <N and 0<= ny <M and array[nx][ny] ==0:
                array[nx][ny] = array[x][y] + 1
                q.append((nx,ny))

bfs(array)

for i in array:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res-1)
