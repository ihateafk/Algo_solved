N = int(input())
P = list(map(int, input().split()))

for n in range(1, N):
    for i in range((n + 1) // 2):
        temp = P[i] + P[n - i - 1]
        if temp > P[n]:
            P[n] = temp

print(P[-1])