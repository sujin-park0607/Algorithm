# 적록색약이 아닌사람 -> 빨강, 파랑 , 초록 
# 적록색약인 사람 -> 빨강-초록, 파랑
# 적록색약인 사람이 봤을때 아닌사람이 봤을때 구역 수
from collections import deque

def rgb_bfs(x,y,type):
    q = deque([(x,y)])
    if type=='rgb': rgb_visited[x][y] = True
    else:rb_visited[x][y] = True 
    

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

                    
            if type == 'rgb':
                 if 0 <= nx < N and 0 <= ny < N and not rgb_visited[nx][ny] and location[x][y] == location[nx][ny]:
                    q.append((nx,ny))
                    rgb_visited[nx][ny] = True
            else:
                if 0 <= nx < N and 0 <= ny < N and not rb_visited[nx][ny] and ((location[x][y] == 'B'  and location[nx][ny] == 'B') or (location[x][y] != 'B'  and location[nx][ny] != 'B')):
                    q.append((nx,ny))
                    rb_visited[nx][ny] = True
                


N = int(input())
location = []
for _ in range(N):
    location.append(list(input()))
rgb_visited = [[False for i in range(N)] for i in range(N)]
rb_visited = [[False for i in range(N)] for i in range(N)]

# print(rgb_visited)
# print(location)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

rb_location = location.copy()
rgb_cnt = 0
rb_cnt = 0
for i in range(N):
    for j in range(N):
        if not rgb_visited[i][j]:
            rgb_bfs(i,j,'rgb')
            rgb_cnt += 1

        if rb_location[i][j] == 'G':
            rb_location[i][j] == 'R'
        if not rb_visited[i][j]:
            rgb_bfs(i,j,'rb')
            rb_cnt += 1

print(rgb_cnt)
print(rb_cnt)

    