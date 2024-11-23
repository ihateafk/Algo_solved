def numberOfcuts(total_L, cutting_L):
    if total_L % cutting_L > 0:
        return total_L // cutting_L
    return total_L // cutting_L - 1

N, C, W = map(int, input().split())
L = [int(input()) for _ in range(N)]
maxL = max(L)

Max = maxL*W
for cuttingLength in range(1, maxL+1):
    total = 0
    for x in range(N):
        if L[x] < cuttingLength: continue
        cutnum = numberOfcuts(L[x], cuttingLength)
        revenue = (L[x] // cuttingLength)*cuttingLength*W - cutnum*C
        if revenue <= 0: continue
        total += revenue
    if total > Max:
        Max = total

print(Max)