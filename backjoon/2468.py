#지녁의 높이 정보 파악
# 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사
# 장마철 비의 양 높이 이하의 모든 지점은 잠김
# 물에 잠기지 않는 안전한 영역의 개수 중에서 최대인 경우는 5 
from collections import deque;

def bfs(x,y,high):
    q = deque([(x,y)])
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and location[nx][ny] > high:
                q.append((nx,ny))
                visited[nx][ny] = True

    return True
                 

N = int(input())
location = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
      location.append(list(map(int,input().split())))

max_cnt = 0
for high in range(101):
    count = 0
    visited = [[False] * N for i in range(N)] 
    for i in range(N):
        for j in range(N):
            if location[i][j] > high and not visited[i][j]:
                bfs(i,j,high)
                count += 1
    # print(count)
    # for v in visited:
    #     print(v)
    if count > max_cnt:
        max_cnt = count
print(max_cnt)