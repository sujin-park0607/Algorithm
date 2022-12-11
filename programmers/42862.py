# 바로 앞번호 학생이나 뒷번호 학생에게만 체육복을 빌려줄 수 있음
# 전체학생 수 n
# 체육복 도난 당한 학생들의 번호가 담긴 배열 lost
# 여벌 체육복을 가져온 학생들의 번호 reserve

def solution(n, lost, reserve):
    answer = 0

    reserve_del = set(reserve) - set(lost)
    lost_del = set(lost) - set(reserve)

    for i in reserve_del:
        if i-1 in lost_del:
            lost_del.remove(i-1)
        elif i+1 in lost_del:
            lost_del.remove(i+1)
    
    answer = n - len(lost_del)
    return answer



