from collections import deque

def bfs(x, y, idx):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx = x+dirx[i]
            dy = y+diry[i]
            if dx < 0 or dx >= N or dy < 0 or dy >= M: continue
            if mapp[dx][dy] == 1: continue
            if visited[dx][dy] == idx: continue
            visited[dx][dy] = idx
            group[idx] += 1
            q.append((dx, dy))

dirx = [-1, 0, 1, 0]
diry = [0, 1, 0, -1]

N, M = map(int, input().split())
mapp = [list(map(int, list(input()))) for _ in range(N)]

group = [0]*(N*M+1)
visited = [[0]*M for _ in range(N)]
idx = 0

for x in range(N):
    for y in range(M):
        if mapp[x][y] == 1: continue
        if visited[x][y] != 0: continue
        idx += 1
        visited[x][y] = idx
        group[idx] = 1
        bfs(x, y, idx)

for x in range(N):
    for y in range(M):
        if mapp[x][y] == 0:
            print(0, end="")
            continue
        check = [0]*4
        Sum = 1
        for i in range(4):
            dx = x+dirx[i]
            dy = y+diry[i]
            if dx < 0 or dx >=N or dy < 0 or dy >= M: continue
            if visited[dx][dy] in check: continue
            check[i] = visited[dx][dy]
            Sum += group[visited[dx][dy]]
        print(Sum%10, end="")
    print()