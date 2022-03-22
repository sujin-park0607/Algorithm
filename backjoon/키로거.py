
test_case = int(input())

for _ in range(test_case):
    string = list(input())
    
    left_stack = []
    right_stack = []

    for x in string:
        if x == '<':
            if len(left_stack) == 0:
                continue
            else:
                pop = left_stack.pop()
                right_stack.append(pop)
        
        elif x == '>':
            if len(right_stack) == 0:
                continue
            else:
                pop = right_stack.pop()
                left_stack.append(pop)
        
        elif x == '-':
            if len(left_stack) == 0:
                continue
            else:
                left_stack.pop()
        
        else:
            left_stack.append(x)
    
    #틀린이유
    left_stack.extend(reversed(right_stack))
    print("".join(left_stack))
                
                

            


