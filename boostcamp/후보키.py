from itertools import combinations

def solution(relation):
    answer = 0
    row = len(relation)
    cols = len(relation[0])

    candidates = []
    for i in range(1, cols+1):
        candidates.extend(combinations(range(cols),i))
    
    unique = []
    for i in candidates:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == row:
            put = True

            for x in unique:
                if set(x).issubset(set(i)):
                    put = False
                    break
            
            if put: unique.append(i)

    return len(unique)


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(relation)