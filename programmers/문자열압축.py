def solution(s):
    
    size = len(s)
    answer = size
    
    for i in range(1,int(size/2+1)):
        result = ""
        before = ""
        cnt = 1
        for j in range(0,size, i):
            temp = s[j:j+i]
            
#             print("temp",temp)
#             print("before",before)
            
            if temp == before:
                cnt += 1
            elif temp != before:
                if cnt > 1:
                    result += str(cnt)
                result += before
                before = temp
                cnt = 1
            
        if cnt > 1:
            result += str(cnt)
        result += before
        
        answer = min(answer,len(result))
        # print("-----------------")
        # print("result",result)
        # print("answer",answer)
        # print()
        
        
    return answer

solution("ababcdcdababcdcd")