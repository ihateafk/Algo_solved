from collections import deque

def rotation(sx, sy, d):
    for k in range(d >> 1):
        val = [mapp[sx+k][sy+i] for i in range(k, d-1-k)]
        iter_val = iter(val)
        for i in range(k, d-1-k):
            mapp[sx + k][sy + i] = mapp[sx + d-1-i][sy + k]
        for i in range(d-1-k, k, -1):
            mapp[sx + i][sy + k] = mapp[sx + d-1-k][sy + i]
        for i in range(d-1-k, k, -1):
            mapp[sx + d-1-k][sy + i] = mapp[sx + d-1-i][sy + d-1-k]
        for i in range(k, d-1-k):
            mapp[sx + i][sy + d-1-k] = next(iter_val)
    return

def shrinking():
    D = 1 << N
    shrink = set()
    for x in range(D):
        for y in range(D):
            if mapp[x][y] == 0: continue
            cnt = 0
            for i in range(4):
                dx = x + dirx[i]
                dy = y + diry[i]
                if dx < 0 or dx >= D or dy < 0 or dy >= D: continue
                if mapp[dx][dy] == 0: continue
                cnt += 1
            if cnt >= 3: continue
            shrink.add(x*D + y)

    while shrink:
        p = shrink.pop()
        x = p // D
        y = p % D
        mapp[x][y] -= 1

    return

def bfs(stx, sty):
    D = 1 << N
    area = mapp[stx][sty]
    mapp[stx][sty] = 0
    cnt = 1

    q = deque()
    q.append(stx*D + sty)
    while q:
        point = q.popleft()
        x = point // D
        y = point % D
        for i in range(4):
            dx = x + dirx[i]
            dy = y + diry[i]
            if dx < 0 or dx >= D or dy < 0 or dy >= D: continue
            if mapp[dx][dy] == 0: continue
            if dx*D + dy in visited: continue
            visited.add(dx*D + dy)
            area += mapp[dx][dy]
            # mapp[dx][dy] = 0
            cnt += 1
            q.append(dx*D + dy)

    return area, cnt


N, Q = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(1 << N)]
order = tuple(map(int, input().split()))
D = 1 << N

dirx = [-1, 0, 1, 0]
diry = [0, 1, 0, -1]

for L in order:
    if L != 0:
        d = 1 << L
        for stx in range(0, D, d):
            for sty in range(0, D, d):
                rotation(stx, sty, d)
    shrinking()

# 면적이랑 칸수 세기
total = 0
big = 0
visited = set()
for x in range(1 << N):
    for y in range(1 << N):
        if mapp[x][y] == 0: continue
        if x*D + y in visited: continue
        visited.add(x * D + y)
        area, cnt = bfs(x, y)
        total += area
        if cnt > big:
            big = cnt

print(total, big, sep="\n")