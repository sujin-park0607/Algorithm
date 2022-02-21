test_case = int(input())

count = []
for i in range(test_case):
    friends = []
    network = int(input())
    for i in range(network):
        input_friend = set(input().split())
        if input_friend in friends or len(friends) == 0:
            friends += input_friend
        else:

        
        
        count.append(len(set(friends)))


for i in count: print(i)

##union-find 알고리즘 -> 원소들의 연결 여부를 확인하는 알고리즘 

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    parent[y] = x

parent = []
for i in range(0,5):
    parent.append(i)


 
