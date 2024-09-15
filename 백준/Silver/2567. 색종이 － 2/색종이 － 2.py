N = int(input())
black = [list(map(int, input().split())) for _ in range(N)]
mapp = [[0]*102 for _ in range(102)]
dir = [-1, 0, 1, 0, 0, -1, 0, 1]

sx = 102
sy = 102
bx = 0
by = 0
for i in range(N):
    stx = black[i][0]+1
    sty = black[i][1]+1
    edx = stx+10
    edy = sty+10
    if stx < sx:
        sx = stx
    if sty < sy:
        sy = sty
    if edx > bx:
        bx = edx
    if edy > by:
        by = edy

    for x in range(stx, edx):
        for y in range(sty, edy):
            if mapp[x][y] == 0:
                mapp[x][y] = 1

lensum = 0
for x in range(sx-1, bx+1):
    for y in range(sy-1, by+1):
        if mapp[x][y] == 1: continue
        for i in range(0, 8, 2):
            dx = x+dir[i]
            dy = y+dir[i+1]
            if dx<sx or dx>bx or dy<sy or dy>by: continue
            if mapp[dx][dy] == 1:
                lensum += 1

print(lensum)