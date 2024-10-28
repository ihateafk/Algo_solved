N = int(input())
arr = list(map(int, input().split()))

result = [1]*N
Max = 1
for x in range(N):
    for y in range(x):
        if arr[x] < arr[y]:
            if result[y]+1 > result[x]:
                result[x] = result[y]+1
    if result[x] > Max:
        Max = result[x]

print(Max)