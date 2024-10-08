N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    idx, val = map(int, input().split())
    arr[idx].append(val)
    arr[val].append(idx)

tree = [0]*(N+1)
tree[0] = 1
tree[1] = 1
stack = [0]*N
top = 0
stack[top] = 1
while top >= 0:
    node = stack[top]
    for x in range(len(arr[node])):
        if tree[arr[node][x]] != 0: continue
        tree[arr[node][x]] = node
        top += 1
        stack[top] = arr[node][x]
        break
    else:
        top -= 1
        continue

for x in range(2, N+1):
    print(tree[x])