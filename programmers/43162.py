
def solution(n, computers):
    graph = {i:[] for i in range(n)}

    for i in range(computers[0]):
        for j in range(computers):
            if(computer[i][j] == 1):
                if i==j:
                    continue
                else:
                    graph[i] = graph[i].get() + [j]
                    graph[j] = graph[j].get() + [i]
    print(graph)


n = 3
computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

solution(n, computers1)
