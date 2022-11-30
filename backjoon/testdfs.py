def dfs(y, x, depth):
    if x < 0 or y < 0 or y >= N or x >= M: #영역초과
        return

    if y == N-1 and x == M-1: #도착
        global Min
        if depth < Min:
            Min = depth
        return

    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        if nx < 0 or ny < 0 or ny >= N or nx >= M:  # 영역초과
            pass
        elif visit[ny][nx] == 0 and map[ny][nx] == '1':
            visit[ny][nx] = 1
            dfs(ny, nx, depth+1)
            visit[ny][nx] = 0


N, M = 10, 10
map = [""] * N
visit = [[0] * M for _ in range(N)]
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

Min = N*M

for i in range(N):
    map[i] = input()

dfs(0,0,1)
print(Min)