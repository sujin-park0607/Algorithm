#최대한 많은 부서의 물품을 구매해줄 수 있도록 함
# 부서가 신청한 금액만큼 모두 지원 
#부서별로 신청한 금액 배열: d
# 예산: budget
#최대로 몇개의 부서에 물품을 지원할 수 있는가?

def solution(d, budget):
    answer = 0
    d = sorted(d)
    
    for i in d:
        if(budget >= i):
            answer +=1
            budget -= i
            
    return answer

print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))