from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0<= ny < N  and array[nx][ny] == 0: #and (nx,ny) not in q
                array[nx][ny] = array[x][y] + 1
                q.append((nx,ny))

    return array[rx][ry]



T = int(input())

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]
q = deque()

for _ in range(T):
    N = int(input())

    array = [[0]*N for _ in range(N)]

    ax, ay = map(int,input().split())
    q.append((ax,ay))

    rx, ry = map(int,input().split())

    if ax == rx and ay == ry:
        print(0)
    else:
        print(bfs())
            

