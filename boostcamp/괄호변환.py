def divide(p):
    left = 0
    right = 0
    
    if not p:
        return ""
    
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        else:
            right += 1

        if left == right:
            u = p[:i+1]
            v = p[i+1:] if i+1 < len(p) else ""
            break
    return u, v

def isCorrect(p):
    stack = []

    correct = True
    for j in p:
        if j == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                correct = False
                return correct
            stack.pop()
    
    return correct



def recursive(p):
    result = ""
    if len(p) == 0:
        return ""

    u, v = divide(p)

    #올바른괄호일경우
    if isCorrect(u):
        result =  u + recursive(v)
    
    #올바르지않은 괄호
    else:
        tmp = "("
        tmp += recursive(v)
        tmp += ")"

        u = u[1:-1]
        for c in u:
            if c == '(':
                tmp += ')'
            else:
                tmp += '('
        result += tmp
    
    return result

def solution(p):
    answer = ''
    answer = recursive(p)
    return answer
    
    
    

    # solution("()))((()")