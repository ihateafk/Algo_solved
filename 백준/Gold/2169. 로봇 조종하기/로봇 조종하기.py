N, M = map(int, input().split())
dp = list(map(int, input().split()))
for y in range(M-1):
    dp[y+1] += dp[y]

for x in range(1, N-1):
    lineX = list(map(int, input().split()))
    # 이전 줄에서 아래로만 내려갔을 때 최대값
    for y in range(M):
        dp[y] += lineX[y]

    # 이전 줄에서 오른쪽, 아래로만 갔을 때 최대값
    dpRight = [dp[0]]
    for y in range(1, M):
        dpRight.append(max(dp[y], dpRight[y-1]+lineX[y]))

    # 이전 줄에서 아래, 왼쪽으로 갔을 때 최대값
    dpLeft = [0]*M
    dpLeft[-1] = dp[-1]
    for y in range(-2, -M-1, -1):
        dpLeft[y] = max(dp[y], dpLeft[y+1]+lineX[y])

    # 합치기
    for y in range(M):
        dp[y] = max(dpRight[y], dpLeft[y])

if N > 1:
    lineX = list(map(int, input().split()))
    dp[0] += lineX[0]
    for y in range(1, M):
        dp[y] = max(dp[y]+lineX[y], dp[y-1]+lineX[y])

print(dp[-1])