N = int(input())
arr = list(map(int, input().split()))
for x in range(N):
    if x%2 == 0:
        if arr[x]%2 != 1:
            print("NO")
            break
    else:
        if arr[x]%2 != 0:
            print("NO")
            break
else:
    print("YES")