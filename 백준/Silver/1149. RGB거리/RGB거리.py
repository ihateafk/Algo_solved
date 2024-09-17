N = int(input())
mapp = [0]*(N+1)
mapp[0] = [0]*3
for x in range(1, N+1):
    mapp[x] = list(map(int, input().split()))

for x in range(1, N+1):
    for y in range(3):
        if mapp[x-1][(y+1)%3] <= mapp[x-1][(y+2)%3]:
            mapp[x][y] += mapp[x-1][(y+1)%3]
        else:
            mapp[x][y] += mapp[x-1][(y+2)%3]

print(min(mapp[N]))