from collections import deque

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    pre, nxt = map(int, input().split())
    arr[pre].append(nxt)

term = [0]*(N+1)
visited = set()
acc = [0]*(N+1)

for pre in range(1, N+1):
    for nxt in arr[pre]:
        acc[nxt] += 1

q = deque()
for lec in range(1, N+1):
    if acc[lec] == 0:
        visited.add(lec)
        term[lec] = 1
        q.append(lec)

while q:
    lec = q.popleft()
    for nxt in arr[lec]:
        if nxt in visited: continue
        if acc[nxt] == 1:
            acc[nxt] = 0
            visited.add(nxt)
            term[nxt] = term[lec] + 1
            q.append(nxt)
        else:
            acc[nxt] -= 1

print(*term[1:])