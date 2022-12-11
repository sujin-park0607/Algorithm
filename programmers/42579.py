def solution(genres, plays):
    answer = []
    genreSet = set(genres)
    album = {i : [0] for i in genreSet}
    result = []
    for i,genre in enumerate(genres):
        album[genre].append((i,plays[i]))
        album[genre][0] += plays[i]

    
    dict = sorted(album.items(), key = lambda item:item[1][0], reverse=True)
    print(dict)
    i = 1
    for key, value in  dict:
        if(i==3):break
        value[1:] = sorted(value[1:], key = lambda value:value[1],reverse=True)
        for cnt, v in enumerate(value[1:]):
            if(cnt == 2): break
            answer.append(v[0])
    print(answer)

    return answer
##여기서 놓친것 플레이리스트에 1개만 들어잇을 수 있음
# solution(["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])