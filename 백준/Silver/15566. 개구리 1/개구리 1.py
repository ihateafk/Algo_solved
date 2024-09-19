def dfs(lev):
    global ans
    if lev == N:
        for x in range(M):
            loca1, loca2, subject = adj_list[x]
            frog1, frog2 = mapp[loca1], mapp[loca2]
            if interest[frog1][subject] == interest[frog2][subject]: continue
            break
        else:
            ans = "YES"
            return True
        return False
    for x in range(2):
        if x == 0 and favor[lev][x] == favor[lev][x+1]: continue
        if mapp[favor[lev][x]] != -1: continue
        mapp[favor[lev][x]] = lev
        if dfs(lev+1): return True
        mapp[favor[lev][x]] = -1

N, M = map(int, input().split())
interest = [list(map(int, input().split())) for _ in range(N)]
favor = [list(map(lambda x: x-1, list(map(int, input().split())))) for _ in range(N)]
adj_list = [list(map(lambda x: x-1, list(map(int, input().split())))) for _ in range(M)]
mapp = [-1]*N

ans = "NO"
dfs(0)

print(ans)
if ans == "YES":
    mapp = list(map(lambda x: x+1, mapp))
    print(*mapp)