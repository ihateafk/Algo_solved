from collections import deque

def solution(board):
    dirx = [-1, 0, 1, 0]
    diry = [0, 1, 0, -1]
    N = len(board)
    M = len(board[0])
    visited = [[-1]*M for _ in range(N)]
    q = deque()
    for x in range(N):
        for y in range(M):
            if board[x][y] == 'R':
                visited[x][y] = 0
                q.append((x, y))
            if board[x][y] == 'G':
                goal = (x, y)
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            for n in range(1, 100):
                dx = x + n*dirx[i]
                dy = y + n*diry[i]
                if dx < 0 or dx >= N or dy < 0 or dy >= M or board[dx][dy] == 'D': break
            dx = x + (n-1)*dirx[i]
            dy = y + (n-1)*diry[i]
            if visited[dx][dy] >= 0: continue
            visited[dx][dy] = visited[x][y] + 1
            if dx == goal[0] and dy == goal[1]:
                return visited[dx][dy]
            q.append((dx, dy))
                
    return -1