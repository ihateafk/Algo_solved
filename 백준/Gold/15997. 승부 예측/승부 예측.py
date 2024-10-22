def dfs(lev):
    if lev == 6:
        rank = {}
        rank_cnt = [0]*4
        p = list(points.values())
        p.sort(reverse=True)
        for key in countries:
            for i in range(4):
                if points[key] == p[i]:
                    rank.setdefault(key, i)
                    rank_cnt[i] += 1
                    break
        for key in countries:
            if rank[key] == 0:
                if rank_cnt[0] > 2:
                    ans[key] += prob[key]*(2/rank_cnt[0])
                else:
                    ans[key] += prob[key]
            elif rank[key] == 1:
                ans[key] += prob[key]*(1/rank_cnt[1])
        return

    home = predict[lev][0]
    away = predict[lev][1]
    for x in range(3):
        if predict[lev][2+x] == 0.0: continue
        probability = predict[lev][2+x]
        for key in countries:
            prob[key] *= probability
        if x == 0:
            points[home] += 3
        elif x == 1:
            points[home] += 1
            points[away] += 1
        else:
            points[away] += 3
        dfs(lev+1)
        for key in countries:
            prob[key] /= probability
        if x == 0:
            points[home] -= 3
        elif x == 1:
            points[home] -= 1
            points[away] -= 1
        else:
            points[away] -= 3


countries = input().split()
prob = {}
points = {}
ans = {}
for country in countries:
    prob.setdefault(country, 1)
    points.setdefault(country, 0)
    ans.setdefault(country, 0)
predict = []
for _ in range(6):
    line = input().split()
    for i in range(2, 5):
        line[i] = float(line[i])
    predict.append(line)
dfs(0)

for country in countries:
    if ans[country] > 1.0:
        ans[country] = 1.0
    print(f"{ans[country]:.10f}")