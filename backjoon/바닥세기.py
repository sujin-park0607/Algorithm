from collections import deque

n, m = map(int,input().split())
array = []
for i in range(n):
    array.append(list(input()))

dx = [0,0,1,-1]
dx = [1,-1,0,0]

def bfs(array,a,b):
    q = deque()
    q.append((a,b))
    
    while q:
        x,y = q.popleft()
        
        if array[x][y] == '-':
            array[x][y] == 0
            for i in range(2):
                nx = x+dx[i]

                if nx < 0 and nx >= m:
                    continue

                if array[nx][y] == '-':
                    array[nx][y] == 0
                    q.append((nx,y))
        
        if array[x][y] == '|':
            array[x][y] == 0
            for i in range(2):
                ny = y+dy[i]

                if ny < 0 and ny >= n:
                    continue

                if array[x][ny] == '|':
                    array[x][ny] == 0
                    q.append(x,ny)
    return array

cnt = 0
for a in range(n):
    for b in range(m):
        if array[a][b] != 0:
            bfs(array,a,b)
            cnt += 1
print(array)
print(cnt)
                
