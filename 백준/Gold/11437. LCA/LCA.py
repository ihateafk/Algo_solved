N = int(input())
adj_list = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

order = []
M = int(input())
for _ in range(M):
    order.append(tuple(map(int, input().split())))

height = [0]*(N+1)
who_is_parent = [1]*(N+1)

# dfs with no recursion
# 부모 체크, 노드의 높이 체크, 인접리스트에서 자식노드의 리스트 중 부모노드 삭제
stack = [1]
visited = set()
while stack:
    now = stack[-1]
    if now not in visited:
        visited.add(now)
        if now != 1:
            adj_list[now].remove(stack[-2])
    height[now] = len(stack)
    if len(adj_list[now]) == 0:
        stack.pop()
        continue
    next = adj_list[now].pop()
    who_is_parent[next] = now
    stack.append(next)

for i in range(M):
    a, b = order[i]
    while a != b:
        if height[a] > height[b]:
            a = who_is_parent[a]
        elif height[a] < height[b]:
            b = who_is_parent[b]
        else:
            a = who_is_parent[a]
            b = who_is_parent[b]
    print(a)