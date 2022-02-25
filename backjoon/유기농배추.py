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

    while True:
        if 0 <= x < N:
            x += 1
        else: y+= 1

        x,y  = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ground[nx][ny] == 1:
                
                ground[x][y] = ground[nx][ny] + 1 
