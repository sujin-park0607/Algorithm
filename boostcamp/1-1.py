keyboard = [["가","호","저","론","남","드","부","이","프","설"],
    ["알","크","청","울","키","초","트","을","배","주"],
    ["개","캠","산","대","단","지","역","구","너","양"],
    ["라","로","권","교","마","쿼","파","송","차","타"],
    ["코","불","레","뉴"," ","서","한","산","리","개"],
    ["터","강","봄","토","캠","상","호","론","운","삼"],
    ["보","람","이","경","아","두","프","바","트","정"],
    ["스","웨","어","쿼","일","소","라","가","나","도"],
    ["판","자","비","우","사","거","왕","태","요","품"],
    ["안","배","차","캐","민","광","재","봇","북","하"]
  ]
  
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

print(solution("부스트캠프"))
print(solution("부슈트캠프"))
print(solution("불레뉴캠프"))
print(solution("뉴$솔레어"))
print(solution("뉴뉴"))