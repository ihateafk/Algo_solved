def find_route(line):
    if group[line] == 0:
        return line
    number = find_route(group[line])
    group[line] = number
    return number

def union(a, b):
    route_a, route_b = find_route(a), find_route(b)
    if route_a == route_b:
        return
    group[route_b] = route_a
    return

def trace_route(x, y):
    while True:
        visited[x][y] = route_num
        dx = x+dir[mapp[x][y]][0]
        dy = y+dir[mapp[x][y]][1]
        if visited[dx][dy] == 0:
            x = dx
            y = dy
            continue
        if visited[dx][dy] == route_num: return
        union(visited[dx][dy], visited[x][y])
        return

N, M = map(int, input().split())
mapp = [input() for _ in range(N)]
group = [0]*(N*M+1)
visited = [[0]*M for _ in range(N)]
dir = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}
route_num = 0
for x in range(N):
    for y in range(M):
        if visited[x][y] != 0: continue
        route_num += 1
        trace_route(x, y)

cnt = 0
for x in range(1, route_num+1):
    if group[x] == 0:
        cnt += 1

print(cnt)