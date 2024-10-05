N, M = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(N)]
order = tuple(tuple(map(int, input().split())) for _ in range(M))

dirx = [0, -1, -1, -1, 0, 1, 1, 1]
diry = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud = set()
for i in range(2):
    for j in range(2):
        cloud.add((N-i-1)*N+j)

ban_area = set()
for d, s in order:
    d -= 1
    # 구름 이동 & 비
    while cloud:
        p = cloud.pop()
        x = p // N
        y = p % N
        x = (x + s * dirx[d]) % N
        y = (y + s * diry[d]) % N
        mapp[x][y] += 1
        ban_area.add(x*N + y)

    # 비가 다 내린 후에 물복사
    for p in ban_area:
        x = p // N
        y = p % N
        cnt = 0
        for i in range(1, 8, 2):
            dx = x + dirx[i]
            dy = y + diry[i]
            if dx < 0 or dx >= N or dy < 0 or dy >= N: continue
            if mapp[dx][dy] == 0: continue
            cnt += 1
        mapp[x][y] += cnt

    # 구름 생성
    for x in range(N):
        for y in range(N):
            if mapp[x][y] < 2: continue
            if x*N + y in ban_area: continue
            mapp[x][y] -= 2
            cloud.add(x*N + y)

    ban_area.clear()

# 물 합산
total = 0
for x in range(N):
    for y in range(N):
        total += mapp[x][y]

print(total)