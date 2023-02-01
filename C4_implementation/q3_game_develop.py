
# 방향 회전을 담당하는 함수
def turn_left():
    global direction
    direction -= 1
    # 북쪽 방향에서 회전했을때는 서쪽을 보게 변수 변경
    if direction == -1:
        direction = 3

# 맵의 가로세로 크기 입력 받음
n, m = map(int, input().split())
# 현재 좌표와 시선 방향 입력 받음
x, y, direction = map(int, input().split())

# 맵 정보 2차원 리스트 초기화
graph = []
# 방문 정보 2차원 리스트 초기화
visited = [[0] * m for _ in range(n)]

# 이동할 좌표를 계산하기 위한 변수 선언(북동남서 순서)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 지도 정보 입력 받음
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 방문 칸수를 기록할 변수 선언
visit_count = 0
# 회전 횟수를 기록할 변수 선언
turn_count = 0

# 출발 좌표 방문 처리
visited[x][y] = 1
# 출발 좌표 방문하면서 방문 횟수 1증가
visit_count += 1

while True:
    # 왼쪽을 회전하고 회전 횟수 기록
    turn_left()
    turn_count += 1
    # 현재 방향으로 전진할 좌표 계산
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 방문하지 않은 육지가 있는 경우
    if graph[nx][ny] == 0 and visited[nx][ny] == 0:
        # 방문 처리
        visited[nx][ny] = 1
        # 좌표 이동
        x, y = nx, ny
        # 방문 횟수 기록
        visit_count += 1
        # 회전 횟수 초기화
        turn_count = 0
        continue

    # 네 번 회전해도 갈 곳이 없는 경우
    if turn_count == 4:
        # 현재 방향으로 후진할 좌표 계산
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 이동 가능한 육지인 경우
        if graph[nx][ny] == 0:
            # 좌표 이동
            x, y = nx, ny
            # 회전 횟수 초기화
            turn_count = 0
        else: # 바다라서 이동할 수 없는 경우
            break

# 결과 출력
print(visit_count)