N, M, V = map(int,input().split(' '))

graph = {}

for _ in range(M):
    a, b = map(int,input().split(' '))
    graph[a] = graph.get(a,[]) + [b]
    graph[b] = graph.get(b,[]) + [a]

print(graph)


def dfs(graph,V):
    visited = list()
    need_visit = list()

    need_visit.append(V)
    while need_visit:
        current = need_visit.pop()
        if current not in visited:
            visited.append(current)
            temp = graph[current]
            temp = sorted(temp, reverse=True)
            need_visit.extend(temp)
    
    return visited

def bfs(graph,V):
    visited = list()
    need_visit = list()

    need_visit.append(V)
    while need_visit:
        current = need_visit.pop(0)
        if current not in visited:
            visited.append(current)
            temp = graph[current]
            temp = sorted(temp)
            need_visit.extend(temp)
    return visited

print(dfs(graph,V))
print(bfs(graph,V))

