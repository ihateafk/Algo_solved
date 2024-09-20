N = int(input())
arr = list(map(int, input().split()))
forward = [1]*N
backward = [1]*N

for x in range(1, N):
    for y in range(x):
        if arr[x] > arr[y]:
            forward[x] = max(forward[y]+1, forward[x])

for x in range(N-2, -1, -1):
    for y in range(N-1, x, -1):
        if arr[x] > arr[y]:
            backward[x] = max(backward[y]+1, backward[x])

Max = forward[0]+backward[0]
for x in range(1, N):
    if forward[x]+backward[x] > Max:
        Max = forward[x]+backward[x]
print(Max-1)