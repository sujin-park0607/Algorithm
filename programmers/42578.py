# 스파이가 가진 의상들이 담긴 2차원 배열clothes가 주어짐
# 서로 다른 옷의 조합의 수 return
#순열 - 순서를 포함한 조합 example) 반장 부반장
#조합 - 순서를 상관하지 않은 조합 ) 학급인원 2 명
from itertools import combinations, product
def solution(clothes):
    answer = 1
    
    dict = {i[1]:["noItems"] for i in clothes}
    result = []
    
    for name, kind in clothes:
        dict[kind].append(name)
    
    for key,value in dict.items():
        answer *= len(value)
    
    answer -= 1
    return answer