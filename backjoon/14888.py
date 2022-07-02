def permutations(arr, n):
    if n == 0:
        yield []
    
    for i, el in enumerate(arr):
        for p in permutations(arr[:i] + arr[i+1:], n-1):
            yield [el] + p
            

def solution():
    N = input()
    AN = list(map(int,input().split(" ")))
    ON = list(map(int,input().split(" ")))

    n = len(AN) - 1
    arr = []    
    for i in range(len(ON)):
        if ON[i] > 0:
            for _ in range(ON[i]):
                arr.append(i)

    minNum = 10e9
    maxNum = -10e9

    
    for per in permutations(arr, n):
        temp = AN[0]
        for num, oper in zip(AN[1:],per):

            if oper == 0:
                temp += num

            elif oper == 1:
                temp -= num

            elif oper == 2:
                temp *= num

            elif oper == 3:
                if temp < 0:
                    temp = (abs(temp)//num) * -1
                else:
                    temp = int(temp//num)

        minNum = min(minNum, temp)
        maxNum = max(maxNum, temp)        
    
    print(maxNum)
    print(minNum)
    
# solution()

arr = ["hello 12345 default", "hihi 12345 use", "muzi 44554 sdfd"]

# {"12345": ["hello 12345 default","hihi 12345 use"], "44554":["muzi 44554 sdfd"]}

dic = {}

for el in arr:
    temp = el.split(" ")
    k = temp[1]
    
    dic[k] = dic.get(k, []) + [el]
print(dic)
