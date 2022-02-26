from collections import deque
import sys

input = sys.stdin.readline
def bfs(graph,start,visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft() 
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

N, M = map(int,input().split())

graph = [[]for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (N+1)
cnt = 0

for i in range(1,N+1):
    if not visited[i]:
        bfs(graph,i,visited)
        cnt += 1
print(cnt)
