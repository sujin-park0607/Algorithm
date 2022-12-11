def solution(participant, completion):
    answer = 0
    list = participant + completion
    dict = { i: 0 for i in list }
    for i in list:
        dict[i] += 1
    
    for key,value in dict.items():
        if not (value%2 ==0):
            return key

solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])
