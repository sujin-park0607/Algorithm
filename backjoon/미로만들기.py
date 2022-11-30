from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = []
N = 10
for i in range(N):
    arr.append(list(map(int, input().strip())))


def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[-1] * N for _ in range(N)]
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        if x == N-1 and y == N-1:
            return visited[x][y]

        #상하좌우 방문
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            #x,y값이 배열이 넘지 않고, 방문한적이 없어야함
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                
                #1일경우 먼저->최단경로가 나와야하기때문
                if arr[nx][ny] == 1:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]

                #0일경우 ->1이 없을경우 검정을 바꿈
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


print(bfs())