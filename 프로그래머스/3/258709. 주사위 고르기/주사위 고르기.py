def solution(dice):
    import itertools
    import math

    def findSumList(who):
        def dfs(lev, Sum):
            if lev == M:
                arr.append(Sum)
                return

            for x in range(6):
                dfs(lev + 1, Sum + dice[who[lev]][x])

        arr = []
        dfs(0, 0)
        return arr

    N = len(dice)
    M = N // 2
    C = set(range(N))
    combIter = itertools.combinations(range(N), N // 2)
    Max = 0

    case = math.comb(N, N // 2)
    for _ in range(case):
        A = next(combIter)
        B = tuple(C - set(A))

        SumListA = findSumList(A)
        SumListB = findSumList(B)

        dicA = {}
        dicB = {}
        SumList = set()
        for x in range(len(SumListA)):
            SumList.add(SumListA[x])

            if dicA.get(SumListA[x]):
                dicA[SumListA[x]] += 1
            else:
                dicA[SumListA[x]] = 1

        for x in range(len(SumListB)):
            SumList.add(SumListB[x])

            if dicB.get(SumListB[x]):
                dicB[SumListB[x]] += 1
            else:
                dicB[SumListB[x]] = 1

        SumList = sorted(SumList)
        indexA = 0
        indexB = 0
        probCount = 0
        for num in SumList:
            if num in dicA and num in dicB:
                if dicA[num] > 0:
                    for _ in range(dicA[num]):
                        probCount += indexB
                else:
                    probCount += indexB
                
                indexA += dicA[num]
                indexB += dicB[num]
            elif num in dicA:
                if dicA[num] > 0:
                    for _ in range(dicA[num]):
                        probCount += indexB
                else:
                    probCount += indexB

                indexA += dicA[num]
            else:  # if num in setB
                indexB += dicB[num]
        print(probCount)
        if probCount >= Max:
            Max = probCount
            answer = A

    answer = list(map(lambda x: x + 1, answer))

    return answer