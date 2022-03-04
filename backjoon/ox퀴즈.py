
t = int(input())


for _ in range(t):

    ox = list(input())
    array = [0 for _ in range(len(ox))]
    
    for i in range(len(ox)):
        if ox[i] == 'O':
            if ox[i-1] == 'O':
                array[i] = array[i-1] + 1
            else:
                array[i] = 1
        else:
            array[i] = 0

    print(sum(array))
    