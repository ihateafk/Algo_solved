from collections import deque

N, M, K = map(int, input().split())
fireballs = deque()
# mapp에 저장되는 값은 개수 질량 속력 방향 순
# 방향은 짝수면 0 홀수면 1씩 더해짐
mapp = [[[0 if i != 1 else -1 for i in range(5)] for _ in range(N)] for _ in range(N)]
for i in range(M):
    x, y, m, s, d = map(int, input().split())
    fireballs.append((x - 1, y - 1, m, s, d))
# 한바퀴 돌았다는 표시
endpoint = (-1, 0, 0, 0, 0)
fireballs.append(endpoint)

dirx = [-1, -1, 0, 1, 1, 1, 0, -1]
diry = [0, 1, 1, 1, 0, -1, -1, -1]
total_mess = 0
visited = set()
iwannadel = set()
# 2개 이상인 mapp coordinate
fusion = set()

k = 0
idx = 0
################# 이동 ################
while k < K:
    x, y, m, s, d = fireballs.popleft()
    if x == -1:
        # 같은 자리에 2개 이상이면 분할 & 이동 & 저장
        while fusion:
            point = fusion.pop()
            x = point // N
            y = point % N
            idx = mapp[x][y][1]
            dm = int(mapp[x][y][2] / 5)
            if dm == 0:
                iwannadel.add(idx)
                continue
            ds = int(mapp[x][y][3] / mapp[x][y][0])
            if mapp[x][y][4] == 0 or mapp[x][y][4] == mapp[x][y][0]:
                dd = 0
            else:
                dd = 1

            # 덱에 불알 추가
            fireballs[idx] = (x, y, dm, ds, dd)
            for i in range(dd+2, 8, 2):
                fireballs.append((x, y, dm, ds, i))

        # 1명령 끝났으니 방문이랑 시작 인덱스 초기화
        iwannadel = list(iwannadel)
        iwannadel.sort(reverse=True)
        for idx in iwannadel:
            del fireballs[idx]
        iwannadel = set()
        visited.clear()
        idx = 0
        k += 1
        fireballs.append(endpoint)
        continue
    # 이동
    dx = (x + s * dirx[d]) % N
    dy = (y + s * diry[d]) % N
    # 개수 질량 속력 방향 갱신
    # # 이번 명령에 방문 안했으면
    if dx * N + dy not in visited:
        mapp[dx][dy][0] = 0
        mapp[dx][dy][1] = -1
        mapp[dx][dy][2] = 0
        mapp[dx][dy][3] = 0
        mapp[dx][dy][4] = 0
    visited.add(dx * N + dy)
    mapp[dx][dy][0] += 1
    mapp[dx][dy][2] += m
    mapp[dx][dy][3] += s
    mapp[dx][dy][4] += d % 2
    # 덱에 불알 추가
    if mapp[dx][dy][0] < 2:
        mapp[dx][dy][1] = idx
        fireballs.append((dx, dy, m, s, d))
        idx += 1
    else:
        fusion.add(dx * N + dy)

for i in range(len(fireballs)):
    total_mess += fireballs[i][2]

print(total_mess)