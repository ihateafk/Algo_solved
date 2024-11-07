for _ in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum = [0]*202
    for x in range(100):
        for y in range(100):
            sum[x] += arr[x][y]
            sum[100+y] += arr[x][y]
            if x == y:
                sum[200] += arr[x][y]
            if x == 99-y:
                sum[201] += arr[x][y]

    print(f"#{test_case} {max(sum)}")