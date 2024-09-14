import heapq

def next_position(case, node, t):
    if case == 0:
        node *= 2
    elif case == 1:
        node -= 1
        t += 1
    else:
        node += 1
        t += 1
    return node, t

def bfs(st, ed):
    q = []
    heapq.heappush(q, (0, st))
    while q:
        time, position = heapq.heappop(q)
        for x in range(3):
            new_pos, new_t = next_position(x, position, time)
            if new_pos == ed:
                return new_t
            if new_pos < 0 or new_pos > 100000: continue
            if new_t >= visited[new_pos]: continue
            visited[new_pos] = new_t
            heapq.heappush(q, (new_t, new_pos))

N, K = map(int, input().split())
visited = [100001]*100001
Min_time = 0
if N != K:
    if N > K:
        Min_time = N - K
    else:
        visited[N] = 0
        Min_time = bfs(N, K)

print(Min_time)