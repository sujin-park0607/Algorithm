from datetime import datetime
import math

def cal(fees, value):
    #홀수인경우 마지막시간 추가
    if len(value) % 2 != 0:
        value.append(['23:59','OUT'])
    #시간정렬
    value = sorted(value, key = lambda x:x[0])
    time = datetime.strptime("00:00","%H:%M")
    
    #순서대로 시간빼기
    for i in range(0,len(value)-1,2):
        time1 = datetime.strptime(value[i][0],"%H:%M")
        time2 = datetime.strptime(value[i+1][0],"%H:%M")
        time += time2 - time1

    total = time.hour * 60 + time.minute
    
    #기본요금 낼경우
    if fees[0] >= total:
        return fees[1]
    #추가요금 계산
    else:
        plus = total - fees[0]
        return math.ceil(plus/fees[2]) * fees[3] + fees[1]
    


def solution(fees, records):
    answer = []
    data = {}
    #딕셔너리로 구현
    for record in records:
        record = record.split(" ")
        data[record[1]] = data.get(record[1],[]) + [record]
    
    data = dict(sorted(data.items()))
    
    for key,value in data.items():
        answer.append(cal(fees,value))
        
    return answer