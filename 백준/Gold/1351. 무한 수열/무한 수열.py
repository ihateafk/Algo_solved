import heapq as hq

N, P, Q = map(int, input().split())
result = 1
if N > 0:
    heap = []
    storage = {}
    heap.append(N)
    iter_ = iter(heap)
    try:
        while True:
            now = next(iter_)
            if now//P != 0:
                if storage.get(now//P) is None:
                    heap.append(now//P)
                    storage.setdefault(now//P, 0)
            if now//Q != 0:
                if storage.get(now // Q) is None:
                    heap.append(now // Q)
                    storage.setdefault(now // Q, 0)
    except StopIteration:
        pass
    storage[0] = 1
    hq.heapify(heap)
    while heap:
        now = hq.heappop(heap)
        storage[now] = storage[now//P] + storage[now//Q]
    result = storage[N]
print(result)