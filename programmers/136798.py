# 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기 구매
# 협약으로 공격력의 제한수치를 정함
# 제한수치보다 큰 공격력을 가질려면 협약기관에서 정한 무기 구매
# 1->1/ 2->2/ 3->2/ 4->3/ 5-> 2

def solution(number, limit, power):
    answer = 0

    for i in range(1,number+1):
        cnt = 0
        for j in range(1,int(i ** (1 / 2))+1):
            if i%j==0:
                cnt += 1
                if((j**2) != i ):
                    cnt += 1
        print(cnt)
        if cnt > limit:
            answer += power
        else:
            answer += cnt

    return answer

print(solution(5,3,2))