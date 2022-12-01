def solution(k, score):
    answer = []
    hall = list()

    for index, i in enumerate(score):
        if index < k:
            hall.append(i)
        elif hall[0] < i:
            hall[0] = i
        hall.sort()
        
        answer.append(hall[0])
    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))