#너비우선탐색 bfs ->정점들과 같은 레벨에 있는 노드들을 먼저 탐색 



#BFS
#need_visi 큐 -> 방문이 필요한 노드들의 정보
#visited 큐 ->방문한 순서들을 큐 

def bfs(graph,start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)
    count = 0
    while need_visit:
        count += 1
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    print(count)
    return visited

graph = dict()

graph['A'] = ['B','C']
graph['B'] = ['A','D']
graph['C'] = ['A','G','H','I']
graph['D'] = ['B','E','F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C','J']
graph['J'] = ['I']


print(bfs(graph,'A'))
#시간복잡도 O(노드 + 간선)
        
