from collections import deque
from copy import copy

def flood_fill():
    q = deque(ground_zero)
    blank_zone = copy(blank)
    while q:
        p = q.popleft()
        x = p//9
        y = p%9
        for i in range(4):
            dx = x + dirx[i]
            dy = y + diry[i]
            if dx < 0 or dx >= N or dy < 0 or dy >= M: continue
            if dx*9 + dy not in blank_zone: continue
            blank_zone.remove(dx*9 + dy)
            q.append(dx*9 + dy)

    return len(blank_zone)


N, M = map(int, input().split())
ground_zero = set()
blank = set()
node_list = []
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        node_list.append(i*9 + j)
        if line[j] == 0:
            blank.add(i*9 + j)
        elif line[j] == 2:
            ground_zero.add(i*9 + j)
dirx = [-1, 0, 0, 1]
diry = [0, -1, 1, 0]

select = []
Max_zone = 0
NM = N*M
for x in range(NM):
    fst = node_list[x]
    if fst not in blank: continue
    blank.remove(fst)
    for y in range(x+1, NM):
        sec = node_list[y]
        if sec not in blank: continue
        blank.remove(sec)
        for z in range(y+1, NM):
            trd = node_list[z]
            if trd not in blank: continue
            blank.remove(trd)

            safe_zone = flood_fill()
            if safe_zone > Max_zone:
                Max_zone = safe_zone

            blank.add(trd)
        blank.add(sec)
    blank.add(fst)

print(Max_zone)