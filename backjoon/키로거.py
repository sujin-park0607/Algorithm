
test_case = int(input())

for _ in range(test_case):
    string = list(input())
    stack = []
    buffer = []
    for s in string:

        if s == '<':
            if len(stack) == 0:
                continue
            else:
                pop = stack.pop()
                buffer.append(pop)
        elif s == '>':
            if len(buffer) == 0:
                continue
            else:
                pop = buffer.pop()
                stack.append(pop)
        elif s == '-':
            if len(stack) == 0:
                continue
            else:
                stack.pop()
        else:
            stack.append(s)
            if len(buffer) != 0:
                for i in buffer:
                    pop = buffer.pop()
                    stack.append(pop)

    print("".join(stack))
