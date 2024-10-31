N = int(input())
Max = [0]*3
Min = [0]*3
dir = [-1, 0, 1]

for _ in range(N):
    arr = tuple(map(int, input().split()))
    dpMax = [0]*3
    dpMin = [900001]*3
    for x in range(3):
        for i in range(3):
            dx = x+dir[i]
            if dx < 0 or dx >= 3: continue
            if Max[x]+arr[dx] > dpMax[dx]:
                dpMax[dx] = Max[x]+arr[dx]
            if Min[x]+arr[dx] < dpMin[dx]:
                dpMin[dx] = Min[x]+arr[dx]
    Max = dpMax
    Min = dpMin

print(f"{max(Max)} {min(Min)}")