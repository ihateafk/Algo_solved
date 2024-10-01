# coordinate transformations
def trans(x, y, d):
    if d == 1:
        x, y = -y, x
    elif d == 2:
        x = -x
        y = -y
    elif d == 3:
        x, y = y, -x
    return x, y

# traversal
def traversal(x, y, d):
    val_y = mapp[x][y]
    val_a = val_y
    mapp[x][y] = 0
    out = 0
    for i in range(1, 3):
        for j in range(-1, 2):
            if i == 1:
                if j == -1:
                    sand = int(val_y*0.01)
                elif j == 0:
                    sand = int(val_y*0.07)
                elif j == 1:
                    sand = int(val_y*0.1)
            elif i == 2:
                if j == 0:
                    sand = int(val_y*0.02)
                else: continue
            point = (trans(i, j, d), trans(-i, j, d))
            for di, dj in point:
                if 0 <= x+di < N and 0 <= y+dj < N:
                    mapp[x+di][y+dj] += sand
                else:
                    out += sand
                val_a -= sand
    sand = int(val_y*0.05)
    i, j = trans(0, 2, d)
    if 0 <= x+i < N and 0 <= y+j < N:
        mapp[x+i][y+j] += sand
    else:
        out += sand
    val_a -= sand
    i, j = trans(0, 1, d)
    if 0 <= x+i < N and 0 <= y+j < N:
        mapp[x+i][y+j] += val_a
    else:
        out += val_a
    return out

N = int(input())
mapp = [list(map(int, input().split())) for _ in range(N)]

# 방향 우 상 좌 하
dirx = [0, -1, 0, 1]
diry = [1, 0, -1, 0]

# 회오리 모양으로 순회
total = 0
x = N//2
y = N//2
for n in range(2, 2*N):
    s = n//2
    d = n%4
    # 문제에서 y 좌표 (x, y)
    for _ in range(s):
        x = x + dirx[d]
        y = y + diry[d]
        total += traversal(x, y, d)
d = (d+1)%4
for _ in range(s):
    x = x + dirx[d]
    y = y + diry[d]
    total += traversal(x, y, d)

print(total)