N, K = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
s = 1
basket = 0

for t in range(1, K+1):
    Max = 0
    Max_i = -1
    for i in range(N):
        if A[i] > basket: continue
        temp = (K-t)*(s+B[i]) - (K-t+1)*s - A[i]
        if temp >= 0:
            if temp > Max:
                Max_i = i
                Max = temp
    if Max_i >= 0:
        basket -= A[Max_i]
        s += B[Max_i]
    else:
        basket += s

print(basket)