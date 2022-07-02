# from collections import deque

# def bfs(v):
#     q = deque([v])
#     while q:
#         v = q.popleft()
#         if not (visited[v]):
#             visited[v] = True
#             list.append(v)
#             for e in array[v]:
#                 if not visited[e]:
#                     q.append(e) 

# n, m = map(int,input().split())
# array = [[] for _ in range(n+1)]
# visited = [False] * (n+1)
# list = []
# for _ in range(m):
#     a, b = map(int,input().split())
#     array[a].append(b)

# for e in array:
#     e.sort()

# for i in range(1,n+1):
#     if len(array[i]) != 0:
#         bfs(i)
#         print(list)


list1 = [3,1]
list2 = [4,2]
total = list()
index = 0

for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] > list2[j]:
            if j==0:
                total = [list2[j]] + list1
                print("11:",list2[j])
                print("1",total)
                continue
            elif index < i:
                total = total[:i] +[list2[j]] + list1[i-1:]
                print("list1[i:] ",list1[i:])
                print("22:",list2[j])
                print("2",total)
        else:
            print("hi")
            if len(total) == 0:
                total = list1 + [list2[j]]
                print("33:",list2[j])
                print("3-1",total)
                continue

            else:
                total = total + [list2[j]]
                print("44:",list2[j])
                print("3-2",total)
            

print(total)
