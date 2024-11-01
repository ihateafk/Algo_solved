N, M = map(int, input().split())
period = [int(input()) for _ in range(N)]
min_period = period[0]
for p in period:
    if p < min_period:
        min_period = p

start = min_period
end = M * min_period
while start <= end:
    time = (start + end) // 2
    cnt = 0
    for i in range(N):
        cnt += time // period[i]
    if cnt < M:
        start = time + 1
    else:
        end = time - 1
        min_time = time

print(min_time)