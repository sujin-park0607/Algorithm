from collections import deque

N, K = map(int, input().split())
MAX = 100001

array = [0] * MAX

def bfs():
    q = deque([N])
    while q:
        now_node = q.popleft()
        if now_node == K:
            return array[now_node]
            
        for next_node in (now_node +1, now_node -1, now_node * 2):
            if 0 <= next_node < MAX and not array[next_node]:
                array[next_node] = array[now_node] + 1
                q.append(next_node)
    
print(bfs())
