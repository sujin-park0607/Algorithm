# 파일명이 포함된 숫자를 반영하는 정렬기능 구현
# HEAD, NUMBER, TAIL
# HEAD기준으로 사전순 정렬, 대소문자 구분 X
# HEAD가 같을 경우, NUMBER의 숫자 순으로 정렬, 앞에 0은 무시
# HEAD, NUMBER 숫자가 같을 경우 입력순
# FILES 1000개 이하

# python 정규식 공부 
import re

def divide(s):
    s = s.lower()
    head = re.match('[\D]+',s)
    number = re.search('[0-9]+',s)
    dFile = [head[0], int(number[0]), s[number.end():]]
    return dFile
    
                
def solution(files):
    answer = []
    fileList = []
    
    for i, file in enumerate(files):
        fileList.append([i]+divide(file))

    fileList = sorted(fileList, key = lambda x:(x[1],x[2]))

    for i in fileList:
        answer.append(files[i[0]])

    return answer