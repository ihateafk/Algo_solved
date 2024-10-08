N = int(input())
arr = list(map(int, input().split()))
arr.sort()
a = 0
b = 0
for x in range(N):
    a += arr[x]
    b += a
print(b)