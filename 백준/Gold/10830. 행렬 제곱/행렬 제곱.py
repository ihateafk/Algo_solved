def mat_mul(mat1, mat2):
    result = [[0]*N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            Sum = 0
            for z in range(N):
                Sum += mat1[x][z]*mat2[z][y]
            result[x][y] = Sum%1000

    return result

N, B = map(int, input().split())
matrix = tuple(tuple(map(int, input().split())) for _ in range(N))
storage = [0]*40

# 지수가 1일 때
storage[1] = matrix
if B & 1:
    result = matrix
else:
    # result에 E 할당
    result = tuple(tuple(1 if x == y else 0 for y in range(N)) for x in range(N))
# 지수 2부터 시작
for exp in range(2, 40):
    storage[exp] = mat_mul(storage[exp-1], storage[exp-1])
    if B < 1 << exp - 1: break
    if B & 1 << exp-1:
        result = mat_mul(result, storage[exp])

for x in range(N):
    for y in range(N):
        print(result[x][y]%1000, end=" ")
    print()