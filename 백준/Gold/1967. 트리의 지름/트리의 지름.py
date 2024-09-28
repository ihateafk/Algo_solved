from collections import deque

def traversal():
    max_diameter = 0
    radius = [0]*(N+1)
    stack = deque()
    stack.append(1)
    visited = [0]*(N+1)
    while stack:
        node = stack[-1]
        if visited[node] == 0:
            if adj_list[node]:
                if visited[adj_list[node][0][0]] == 0:
                    n = len(adj_list[node])
                    for i in range(n):
                        stack.append(adj_list[node][i][0])
                    continue
        # 리프노드 이거나 부모노드 이면
        n = len(adj_list[node])
        visited[node] = 1
        stack.pop()
        diameter = 0
        length = [0]*n
        for i in range(n):
            son, cost = adj_list[node][i]
            length[i] = cost+radius[son]
        length.sort(reverse=True)
        if n > 0:
            diameter += length[0]
            if n > 1:
                diameter += length[1]
            radius[node] = length[0]
        max_diameter = max(diameter, max_diameter)

    return max_diameter

N = int(input())
adj_list = [[] for _ in range(N+1)]
for _ in range(N-1):
    parent, son, cost = map(int, input().split())
    adj_list[parent].append((son, cost))

diameter = traversal()

print(diameter)