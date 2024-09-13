import heapq

N = int(input())
arr = [int(input()) for _ in range(N)]
pos = []
neg = []
zero = 0
Sum = 0
for x in range(N):
    if arr[x] > 0:
        heapq.heappush(pos, -arr[x])
    elif arr[x] < 0:
        heapq.heappush(neg, arr[x])
    else:
        zero += 1
P = len(pos)
N = len(neg)
while N > 1:
    Sum += heapq.heappop(neg)*heapq.heappop(neg)
    N -= 2
if N and zero == 0:
    Sum += heapq.heappop(neg)
while P:
    if P < 2:
        Sum += -heapq.heappop(pos)
        P -= 1
        continue
    a, b = -heapq.heappop(pos), -heapq.heappop(pos)
    if a != 1 and b != 1:
        Sum += a*b
    else:
        Sum += a+b
    P -= 2
print(Sum)