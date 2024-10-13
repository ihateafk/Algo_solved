import heapq as hq

def find_head(node):
    if group[node] == 0:
        return node
    head = find_head(group[node])
    group[node] = head
    return head

def union(a, b):
    global cnt
    ha, hb = find_head(a), find_head(b)
    if ha == hb:
        return False
    group[hb] = ha
    cnt += 1
    return True

V, E = map(int, input().split())
cost_heap = []
for _ in range(E):
    a, b, c = map(int, input().split())
    hq.heappush(cost_heap, (c, a, b))
group = [0]*(V+1)

total = 0
cnt = 0
for _ in range(E):
    cost, st, ed = hq.heappop(cost_heap)
    if union(st, ed):
        total += cost
    if cnt + 1 >= V: break

print(total)