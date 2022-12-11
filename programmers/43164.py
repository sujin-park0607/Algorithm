def solution(tickets):
    graph = dict()
    for a,b in tickets:
        graph[a] = sorted(graph.get(a,[]) + [b], reverse=True)
    result = dfs(graph)
    return result

def dfs(graph):
    stack = ["ICN"]
    visited = []
    result = []   
    while stack:
        current = stack.pop()
        result.append(current)
        if current not in graph.keys():
                break
        if current not in visited:
            visited.append(current)
            stack.extend(graph[current])
    return result
    

tickets1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets3 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets4 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(solution(tickets1))
print(solution(tickets2))