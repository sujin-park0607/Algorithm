
  
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
  
def find_pos(chr):
    result = []
    for y, row in enumerate(keyboard):
        if chr in row:
            result.append( (y, row.index(chr)) )
    return result

result = []

def bfs(pos, chr):
    visited = [[False] * 10 for _ in range(10)]

    dq = [(pos[0], pos[1], 0)]
    result = 10e9
    while dq:
        y, x, d = dq.pop(0)

        if keyboard[y][x] == chr:
            if d < result:
                result = d
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < 10 and 0 <= nx < 10:
                if not visited[ny][nx]:
                    dq.append((ny, nx, d+1))
                    visited[ny][nx] = True
    return result


def solution(word):
    answer = [0, 0]

    positions = []
    
    for w in word:
        poses = find_pos(w)
        positions.append(poses)

    for idx in range(len(positions)-1):
        dis = 20
        temp = []
        if (positions[idx] and positions[idx+1]):
            for posA in positions[idx]:
                temp.append(bfs(posA, word[idx+1]))

            answer[1] += 1
            dis = min(temp)
        
        answer[0] += dis

    return answer

