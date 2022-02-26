from collections import deque

def bfs(array, a, b):
    q = deque()
    q.append((a,b))
    ground[a][b] = 0
    
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx>= N or ny<0 or ny>=M:
                continue
            
            if ground[nx][ny] == 1:
                ground[nx][ny] = 0
                q.append((nx,ny))
    return


T = int(input())

dx = [0,0,1,-1]
dy = [1,-1,0,0]
for _ in range(T):
    N, M, K = map(int, input().split())
    cnt = 0

    ground = [[0]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        ground[x][y] = 1

    for a in range(N):
        for b in range(M):
            if ground[a][b] == 1:
                bfs(ground,a,b)
                cnt += 1

    print(cnt) 




    
