from collections import deque

T = int(input())
M, N, K = map(int,input().split())

ground = []
for _ in range(K):
    x, y = map(int, input().split())
    ground.append((x,y))

def dsf(array):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    x, y = 0,0

    q = deque()
    q.append((x,y))

    while q:
        x,y  = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx >= M or ny <0 or ny >= N:
                continue
            
            if ground[nx][ny] == 1:
                if ground[nx][ny] not in q:
                    q.append((nx,ny))
                    ground[x][y] = ground[nx][ny] + 1
    return ground

print(dsf(ground)) 
