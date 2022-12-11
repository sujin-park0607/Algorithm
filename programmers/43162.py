def dfs(graph, start):
    stack = [start]

    while stack:
        current = stack.pop()
        
        if not visited[current]:
            visited[current] = True
            stack.extend(graph[current])

def solution(n, computers):

    col = len(computers[0])
    row = len(computers)

    graph = {i:[] for i in range(n)}

    for i in range(row):
        for j in range(col):
            if computers[i][j] == 1 and i != j:
                graph[i] = graph.get(i) + [j]
    
    global visited
    visited = [False for i in range(n)]

    result = 0
    for i in range(n):
        if not visited[i]:
            result += 1
            dfs(graph, i)
    return result


n = 3
computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n, computers2))
