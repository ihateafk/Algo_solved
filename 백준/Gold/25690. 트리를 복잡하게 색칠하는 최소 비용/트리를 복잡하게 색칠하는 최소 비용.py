from collections import deque

N = int(input())
adj_list = [[] for _ in range(N)]
who_is_parent = [0]*N
# leaf = set(range(N))
for _ in range(N-1):
    p, s = map(int, input().split())
    adj_list[p].append(s)
    who_is_parent[s] = p
    # leaf.discard(p)

cost = []
for node in range(N):
    w, b = map(int, input().split())
    cost.append([w, b])

q = deque()
node = 0
q.append(0)
for i in range(N):
    node = q[i]
    for son in adj_list[node]:
        q.append(son)

# 리프에서 부모로 bottom-up 순회 & 높이별 bfs
while q:
    node = q.pop()
    if node == 0: continue
    parent = who_is_parent[node]
    cost[parent][0] += min(cost[node][0], cost[node][1])
    cost[parent][1] += cost[node][0]
    cost[node][0] = 0
    cost[node][1] = 0

print(min(cost[0]))