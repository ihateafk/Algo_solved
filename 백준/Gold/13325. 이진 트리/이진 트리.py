k = int(input())
weight = [0]*2
weight[2:] = list(map(int, input().split()))
dp = [0]*(len(weight))
ans = 0

for lev in range(k, 0, -1):
    for node in range(1 << lev, 1 << (lev+1), 2):
        p_node = node // 2
        s_node = node + 1
        if weight[node]+dp[node] >= weight[s_node]+dp[s_node]:
            dp[p_node] = weight[node]+dp[node]
        else:
            dp[p_node] = weight[s_node]+dp[s_node]
        ans += dp[p_node]*2 - dp[node] - dp[s_node]

print(ans)