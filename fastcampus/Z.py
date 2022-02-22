# from unittest import result


# n, r, c = map(int,input().split())
# m = 2**n

# row = 0
# col = 0
# array = [[0]* m] * m
# i = 0
# for n in range(1):
#     array[col][row] = i
#     print(array)

#     # print(row+1, col+1, i)
#     col += 1 ; i += 1
#     array[col][row] = i
#     print(array)

#     row += 1 ; col -= 1; i += 1
#     array[col][row] = i
#     col += 1 ; i += 1
#     print(array)
#     # print(row+1, col+1, i)

#     array[col][row] = i
#     print(array)

# print(array)

##################
 
def solve(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y +1 == Y:
            print(result)
            return
        result += 1
        if x + 1 ==X and y ==Y :
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return

    solve(n/2, x, y)
    solve(n/2, x, y+n/2)
    solve(n/2, x + n/2, y)
    solve(n/2, x+ n/2, y+n/2)

result = 0
N, X, Y = map(int,input().split(' '))
solve(2 ** N, 0, 0)
        


