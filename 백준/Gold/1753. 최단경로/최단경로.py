import heapq as hq

V, E = map(int, input().split())
K = int(input())
adjList = [{} for _ in range(V+1)]
for _ in range(E):
    st, ed, w = map(int, input().split())
    if adjList[st].get(ed) is not None:
        if w < adjList[st][ed]:
            adjList[st][ed] = w
    else:
        adjList[st][ed] = w

result = [3000001]*(V+1)
result[K] = 0
heap = []
hq.heappush(heap, (0, K))
while heap:
    cost, layover = hq.heappop(heap)
    if cost > result[layover]: continue

    for ed, w in adjList[layover].items():
        if cost + w < result[ed]:
            result[ed] = cost + w
            hq.heappush(heap, (result[ed], ed))

for i in range(1, V+1):
    if result[i] >= 3000001:
        print('INF')
    else:
        print(result[i])