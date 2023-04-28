#구현 - 빙고
bingo = []
bingo_bol = []
for i in range(5):
    bingo.append(list(map(int, input().split())))
    bingo_bol.append([False for i in range(5)])

print(bingo_bol)
    
