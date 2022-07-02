def divide(p):
    left = 0
    right = 0
    
    for i in range(len(p)):
        if p[i] =='(':
            left += 1
        elif p[i] == ')':
            right += 1
        
        if left == right:
            u = p[:i+1]
            v = p[i+1:]
            return u,v
    
    
    
def solution(p):

    if len(p) == 0:
        return ""
    u, v = divide(p)

    
    stack = []
    isCorrect = True
    for i in u:
        if i == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                isCorrect = False
                break
            else:
                stack.pop()
                
    if len(stack) != 0:
        isCorrect = False
    
            
    if isCorrect:
        return u + solution(v)
    else:
        temp = '('
        temp += solution(v)
        temp += ')'
        
        u = u[1:-1]
        for c in u:
            if c == '(':
                temp += ')'
            else:
                temp += '('
            
    return temp


solution("()))((()")