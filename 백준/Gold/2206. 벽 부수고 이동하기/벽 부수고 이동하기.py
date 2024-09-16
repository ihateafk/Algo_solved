from collections import deque

def bfs():
    q = deque()
    q.append((0, 0, 0))
    while q:
        # broke 1 이면 이전에 부신적 있음
        x, y, broke = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][broke]
        for i in range(0, 8, 2):
            dx = x+dir[i]
            dy = y+dir[i+1]
            if dx < 0 or dx >= N or dy < 0 or dy >= M: continue
            # mapp 0 이고 broke 0 이면 visited 0만 비교하고 값 넣기
            # mapp 0 이고 broke 1 이면 visited 0과 1 모두 비교하고 값 넣기
            # mapp 1 이면 벽 부시고 값 넣기
            if mapp[dx][dy] == 1:
                if broke == 1: continue
                if visited[x][y][0]+1 >= visited[dx][dy][1]: continue
                visited[dx][dy][1] = visited[x][y][0] + 1
                q.append((dx, dy, 1))
                continue
            if visited[x][y][broke]+1 >= visited[dx][dy][broke]: continue
            if broke == 1:
                if visited[x][y][broke]+1 >= visited[dx][dy][0]: continue
            visited[dx][dy][broke] = visited[x][y][broke] + 1
            q.append((dx, dy, broke))
    return -1


dir = [-1, 0, 0, 1, 1, 0, 0, -1]

N, M = map(int, input().split())
mapp = [list(map(int, list(input()))) for _ in range(N)]
visited = [[[1000001]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0]=visited[0][0][1] = 1
ans = bfs()
print(ans)