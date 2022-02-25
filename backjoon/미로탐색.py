from collections import deque


N, M = map(int,input().split())

mirror = []

for _ in range(N):
    mirror.append(list(map(int,input())))


def bfs(x,y):
    #상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=N or ny < 0 or ny >=M:
                continue
            
            if mirror[nx][ny] == 0:
                continue
            
            if mirror[nx][ny] == 1:
                mirror[nx][ny] = mirror[x][y] + 1
                q.append((nx,ny))
        
    return mirror[N-1][M-1]

print(bfs(0,0))            
            