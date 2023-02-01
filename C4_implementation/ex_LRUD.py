# 공간 크기 입력 받음
n = int(input())
# 이동 명령어 입력 받음
commands = input().split()

# 명령어 별로 이동할 좌표를 계산하기 위한 변수 선언(좌우상하 순서)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 주어진 명령어 리스트 선언
cmd = ['L','R','U','D']

# 현재 좌표를 저장할 변수 선언
x, y = 1,1

# 입력한 명령어 개수만큼 반복
for command in commands:
    # 주어진 명령어 개수만큼 반복
    for i in range(4):
        # 주어진 명령어 중에 현재 명령어가 있는지 확인
        if command == cmd[i]:
            # 방향에 맞춰 이동해야할 좌표 계산
            nx = x + dx[i]
            ny = y + dy[i]

            # 계산된 좌표가 주어진 공간안에 정상적으로 있는 경우
            if 0 < nx <= n and 0 < ny <= n:
                x, y = nx, ny

# 결과 출력
print(x, y)