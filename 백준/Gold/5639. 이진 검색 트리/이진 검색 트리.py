from collections import deque

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break
N = len(arr)
adj_list = [[-1]*2 for _ in range(N)]

# 인접리스트 만들기
stack = deque()
stack.append(0)
i = 1
while i < N:
    now = stack[-1]
    if arr[i] < arr[now]:
        adj_list[now][0] = i
        stack.append(i)
        i += 1
    else: # arr[i] > arr[now]
        for r in range(len(stack)):
            if arr[stack[r]] < arr[i]:
                adj_list[stack[r]][1] = i
                break
        for _ in range(r, len(stack)):
            del stack[r]
        stack.append(i)
        i += 1

stack.clear()
# 후위 탐색
stack.append(0)
visited = set()
while stack:
    now = stack[-1]
    flag = True
    for i in range(1, -1, -1):
        if adj_list[now][i] == -1: continue
        if adj_list[now][i] in visited: continue
        stack.append(adj_list[now][i])
        flag = False
    if flag:
        node = stack.pop()
        visited.add(node)
        print(arr[node])