C, P = map(int, input().split())
mapp = list(map(int, input().split()))
# 회전 가짓수, 밑바닥 칸수, [높이 차이, ...]
block = [
    0,
    (2, (1, 0), (4, 0, 0, 0)),
    (1, (2, 0, 0)),
    (2, (3, 0, 1), (2, -1)),
    (2, (3, -1, 0), (2, 1)),
    (4, (3, 0, 0), (2, 1), (3, -1, 1), (2, -1)),
    (4, (3, 0, 0), (2, 0), (3, 1, 0), (2, -2)),
    (4, (3, 0, 0), (2, 2), (3, 0, -1), (2, 0))
]
cnt = 0
# 인접열 높이 차이 배열
diff_map = [0]*(C-1)
for x in range(C-1):
    diff_map[x] = mapp[x+1]-mapp[x]

# 떼뜨리쓰
for n in range(1, block[P][0]+1):
    pattern = block[P][n]
    L = pattern[0]-1
    if L == 0:
        cnt += C
        continue

    for start in range(C-L):
        for x in range(L):
            if diff_map[start+x] != pattern[x+1]: break
        else:
            cnt += 1

print(cnt)