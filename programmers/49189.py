from collections import deque

def solution(n, edge):
    graph = {i:[] for i in range(1, n+1)}
    global visited
    visited = [0 for i in range(n+1)]
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    result = bfs(graph)
    return result.count(max(result))

def bfs(graph):
    q = deque()
    q.append((1,0))

    while q:
        index, count = q.popleft()
        # print(current)
        
        if not visited[index]:
            count += 1
            visited[index] = count
            for num in graph[index]:
                q.append((num,count)) 
    
    return visited
            
    
    
        


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))