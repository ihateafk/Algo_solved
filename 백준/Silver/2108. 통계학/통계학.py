import heapq as hq
from math import floor

N = int(input())
arr = [int(input()) for _ in range(N)]
plus = [0]*4001
minus = [0]*4001

for num in arr:
    if num >= 0:
        plus[num] += 1
    else:
        minus[-num] += 1
# 1
Sum = 0
# 2
middle_i = N // 2 + 1
middle_cnt = 0
median = -4001
# 3
maxCnt = 0
heap = []
# 4
Min = 4001
Max = -4001


for x in range(4000, 0, -1):
    if minus[x] > 0:
        # 1
        Sum += -x * minus[x]
        # 2
        if median < -4000:
            middle_cnt += minus[x]
            if middle_cnt >= middle_i:
                median = -x
        # 3
        if minus[x] >= maxCnt:
            maxCnt = minus[x]
            hq.heappush(heap, (-maxCnt, -x))
        # 4
        if -x > Max:
            Max = -x
        if -x < Min:
            Min = -x

for x in range(4001):
    if plus[x] > 0:
        # 1
        Sum += x * plus[x]
        # 2
        if median < -4000:
            middle_cnt += plus[x]
            if middle_cnt >= middle_i:
                median = x
        # 3
        if plus[x] >= maxCnt:
            maxCnt = plus[x]
            hq.heappush(heap, (-maxCnt, x))
        # 4
        if x > Max:
            Max = x
        if x < Min:
            Min = x

mean = floor(Sum / N + 0.5)

_, mode = hq.heappop(heap)
if heap:
    cnt, num = hq.heappop(heap)
    if -cnt == maxCnt:
        mode = num

print(mean, median, mode, Max - Min, sep='\n')