N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for m in range(N):
    for s in range(N):
        for e in range(N):
            if arr[s][m] and arr[m][e]:
                arr[s][e] = 1

for i in range(N):
    print(*arr[i])