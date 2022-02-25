 #다익스트라 알고리즘 
 #1.초기화
import heapq

mygraph = {
    'A':{'B':8,'C':1,'D':2},
    'B':{},
    'C':{'B':5,'C':2},
    'D':{'E':3,'F':5},
    'E':{'F':1},
    'F':{'A':5}
}

def aa(graph,start):
    distances = {node:float('inf') for node in graph}
    distances[start] = 0
    queue = []

    heapq.heappush(queue,[distances[start],start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for node_name, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[node_name]:
                distances[node_name] = distance
                heapq.heappush(queue,[distance,node_name])
    
    return distances

print(aa(mygraph,'A'))
