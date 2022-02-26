from collections import deque
import sys

# input = sys.stdin.readline()

N = int(input())
array = []
for _ in range(N):
    array.append(list(map(int,input())))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(array, a, b,num):
    q = deque()
    q.append((a,b))
    array[a][b] = num
    visit_cnt = 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if array[nx][ny] == 0:
                continue

            if array[nx][ny] == 1 and (nx,ny) not in q:
                array[nx][ny] = num
                q.append((nx,ny))
                visit_cnt += 1

    return visit_cnt

num = 2
cnt = 0
visited = []
for a in range(N):
    for b in range(N):
        if array[a][b] == 1:
            visited.append(bfs(array,a,b,num))
            num += 1
print(len(visited))


for i in sorted(visited):
    print(i)
            



    