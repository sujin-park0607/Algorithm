from collections import deque

def bfs(maps):
    q = deque()
    q.append((0,0))
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx,ny))
    return maps

def solution(maps):
    maps = bfs(maps)
    result = maps[len(maps)-1][len(maps[0])-1]
    if result == 1:
        return -1
    else:
         return result 

maps1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps1))
print(solution(maps2))
    
    
    