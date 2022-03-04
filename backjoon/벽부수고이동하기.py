from collections import deque
n, m = map(int,input().split())

array = []
for _ in range(n):
    array.append(list(map(int,input())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(array,a,b):
    q = deque()
    q.append((a,b))
  

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>= m or ny<0 or ny>= n:
                continue

            if array[nx][ny] == 0 and (nx,ny) not in q:
                array[x][y] += 1 
                q.append((nx,ny))
   
    return array 

for a in range(m):
    for b in range(n):
        if array[a][b] == 1:
            print(a,b)
            result = bfs(array,a,b)

print(result)