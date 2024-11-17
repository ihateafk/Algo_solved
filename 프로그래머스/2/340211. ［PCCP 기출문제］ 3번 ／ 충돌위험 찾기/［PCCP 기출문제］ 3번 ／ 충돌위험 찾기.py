def solution(points, routes):
    # initialization
    answer = 0
    N = len(points)
    M = len(routes)
    visited = set()
    warn = set()
    curLoc = [0]*M
    arrived = set()
    nextGoal = [1]*M
    moving = set(range(M))
    for robo in range(M):
        logistics = routes[robo][0] - 1
        x, y = map(lambda p: p-1, points[logistics])
        if x*100 + y in visited:
            warn.add(x*100 + y)
        else:
            visited.add(x*100 + y)

        curLoc[robo] = x*100 + y

    answer += len(warn)

    # Main 이동 > 위험 판정
    while moving:
        visited.clear()
        warn.clear()
        for robo in moving:
            # 다음 갈곳 이동하기
            ## 갈 곳 목표 확인하기 물류세터 어디까지 갔었는지 알기 위해 goals 배열 사용
            ## goals[i]는 i+1번 현재 로봇이 가고 있는 routes의 인덱스
            loc = curLoc[robo]
            x = loc//100
            y = loc%100
            if nextGoal[robo] >= len(routes[robo]):
                arrived.add(robo)
                continue
            logistics = routes[robo][nextGoal[robo]] - 1
            gx = points[logistics][0]-1
            gy = points[logistics][1]-1
            ### 갈 방향 확인하기
            ### 현재 위치를 알아야 하는 curLoc 배열 사용
            ### curLoc[i]는 i+1 로봇의 움직이기 전 위치
            ### x 좌표가 다르면 x좌표로 이동 같으면 y 좌표로 이동
            if x != gx:
                if x > gx:
                    x -= 1
                else: # x < gx
                    x += 1
            elif y != gy:
                if y > gy:
                    y -= 1
                else:  # y < gx
                    y += 1
            # 이동한 위치가 물류센터이면 다음 물류센터로 변경
            if x == gx and y == gy:
                nextGoal[robo] += 1

            # 같은 시간에 중복되어 있는지 체크
            ## 이동하고 혹은 이동하기 전에 visited set에 있으면 warn 세트에 저장하기
            if x * 100 + y in visited:
                warn.add(x * 100 + y)
            else:
                visited.add(x * 100 + y)

            curLoc[robo] = x * 100 + y
        ## answer에 len(warn)을 더하고 visited, warn 초기화
        answer += len(warn)

        # 도착한 로봇들 움직이고 있는 로봇 목록에서 빼주기
        moving.difference_update(arrived)

    return answer