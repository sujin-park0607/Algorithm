from collections import deque

N, M = 10,10
array = []
for _ in range(N):
    array.append(list(map(int,input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(array,x,y):
    q = deque()
    q.append((x,y))
    visited = [[-1] * N for _ in range(N)]
    
    count = 0
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            
            if array[nx][ny] == 0:
                continue
            
            if array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1
                q.append((nx,ny))
        count += 1
    
    #return array[N-1][M-1], count
    return array

array = bfs(array,0,0)

for i in array:
    print(i)
        
        