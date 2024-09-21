def trace_route(x, y):
    global cnt
    while True:
        visited[x][y] = route_num
        dx = x+dir[mapp[x][y]][0]
        dy = y+dir[mapp[x][y]][1]
        if visited[dx][dy] == 0:
            x = dx
            y = dy
            continue
        if visited[dx][dy] == route_num:
            cnt += 1
        return

N, M = map(int, input().split())
mapp = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dir = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

route_num = 0
cnt = 0
for x in range(N):
    for y in range(M):
        if visited[x][y] != 0: continue
        route_num += 1
        trace_route(x, y)

print(cnt)