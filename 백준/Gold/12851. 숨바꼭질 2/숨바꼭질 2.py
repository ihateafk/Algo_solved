from collections import deque

def cal_dx(idx, x):
    if idx == 0:
        return x + 1
    if idx == 1:
        return x - 1
    return x << 1

def bfs(start):
    q = deque()
    visited = [0] * 100001
    min_time = 100001
    cnt = 0
    q.append((1, start))
    visited[start] = 1

    while q:
        time, x = q.popleft()
        for i in range(3):
            dx = cal_dx(i, x)
            if dx < 0 or dx > 100000: continue
            if visited[dx] != 0 and visited[dx] < time+1: continue
            if time+1 > min_time: continue
            if dx == K:
                min_time = time+1
                cnt += 1
                continue
            visited[dx] = time+1
            q.append((time+1, dx))
    return min_time-1, cnt

N, K = map(int, input().split())
if N == K:
    time = 0
    cnt = 1
else:
    time, cnt = bfs(N)
print(time, cnt, sep="\n")