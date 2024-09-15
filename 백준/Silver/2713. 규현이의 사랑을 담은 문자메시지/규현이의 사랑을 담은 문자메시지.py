def encrypt(chr):
    if ord(chr) == ord(" "):
        return 0
    return ord(chr) - ord("A") + 1

T = int(input())
for tc in range(1, T+1):
    input1 = input()
    input2 = input1.split()
    R = int(input2[0])
    C = int(input2[1])
    msg = input1[len(input2[0])+len(input2[1])+2:]
    N = len(msg)
    arr = ["0"]*(R*C)
    # chang string to binary
    bi = ""
    for x in range(N):
        dec = encrypt(msg[x])
        for y in range(4, -1, -1):
            if dec & 1 << y:
                bi += "1"
            else:
                bi += "0"
    # fill arr
    visited = [[0]*C for _ in range(R)]
    x = 0
    y = -1
    iter_bi = iter(bi)
    n = 0
    N *= 5
    try:
        while n < N:
            for y in range(y+1, C):
                if visited[x][y] == 1:
                    y -= 1
                    break
                visited[x][y] = 1
                arr[x*C + y] = next(iter_bi)
                n += 1
            for x in range(x+1, R):
                if visited[x][y] == 1:
                    x -= 1
                    break
                visited[x][y] = 1
                arr[x * C + y] = next(iter_bi)
                n += 1
            for y in range(y-1, -1, -1):
                if visited[x][y] == 1:
                    y += 1
                    break
                visited[x][y] = 1
                arr[x * C + y] = next(iter_bi)
                n += 1
            for x in range(x-1, -1, -1):
                if visited[x][y] == 1:
                    x += 1
                    break
                visited[x][y] = 1
                arr[x * C + y] = next(iter_bi)
                n += 1
    except StopIteration:
        pass

    print(*arr, sep="")