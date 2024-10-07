from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited = [0]*(N+1)
    result = set()
    ref = Y % 2
    if len(adj_list[start]) and visited[start] == ref:
        result.add(start)

    while q:
        p = q.popleft()
        past = p // 1000
        now = p % 1000
        if visited[now] > Y: break
        for next in adj_list[now]:
            if next == past: continue
            visited[next] = visited[now]+1
            if visited[next] % 2 == ref:
                result.add(next)
            q.append(now*1000 + next)
    if len(result) == 0:
        print(-1)
    else:
        result = list(result)
        result.sort()
        print(*result)
    return

N, M, X, Y = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

bfs(X)