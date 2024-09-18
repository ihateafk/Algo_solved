def little_star(center, h):
    for i in range(3):
        for j in range(i+1):
            if i == 1 and j == 0: continue
            starTree[h+i][center-j] = "*"
            starTree[h+i][center+j] = "*"

def painting_star(lev, start, h):
    if lev == 0:
        little_star(start, h)
        return
    painting_star(lev-1, start, h)
    painting_star(lev-1, start-(3 << lev-1), h+(3 << lev-1))
    painting_star(lev-1, start+(3 << lev-1), h+(3 << lev-1))

H = int(input())
N = H//3
for x in range(11):
    if N & 1 << x:
        K = x
        break
starTree = [[" "]*(2*H-1) for _ in range(H)]

painting_star(K, H-1, 0)

for line in starTree:
    print(*line, sep="")