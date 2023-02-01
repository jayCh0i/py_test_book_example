# 각 좌표마다 탐색을 실시하면서 구멍이 뚫려있는 부분에 한번 탐색이 실시되면 연결된 좌표들은
# 모두 방문 처리되어 다음에 중복처리 되지 않으며 탐색이 완료되었을 때 아이스크림 개수를 증가시켜주면 된다.
## 입력받는 그래프 데이터가 인접 리스트 형식이 아니라 단순 2차원 리스트로만 주어지기 때문에,
## 한 칸 옆에 인접해 있는 노드들을 처리하려면 직접 좌표값을 계산해서 다음 연산으로 이어가야 한다
### 방문 여부 리스트는 그래프 리스트의 원소 값들이 0, 1인 것을 활용하여 대체한다

# BFS로만 풀어야 되는 문제인줄 알았는데 특별한 이유는 없는듯

from collections import deque

# 1칸 인접한 노드들의 좌표를 계산하기 위한 변수 선언(상하좌우 순서)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    # 그래프 범위를 벗어나면서, 칸막이 및 방문한 칸인경우
    if not (0 <= x < n and 0 <= y < m and graph[x][y] == 0):
        return False

    # 현재 노드 방문 처리
    graph[x][y] = 1

    for i in range(4):
        # 방향별로 인접한 노드의 좌표계산
        nx = x + dx[i]
        ny = y + dy[i]
        # 인접 노드 재귀 호출
        dfs(nx, ny)

    # 참을 반환하여 칸을 채웠음을 알림
    return True

def bfs(x,y):
    # 칸막이거나 방문했던 칸이면 중지
    if graph[x][y] == 1:
        return False
    
    # 큐로 사용할 리스트 선언과 동시에 시작점를 첫 원소로 추가한다.
    q = deque([(x,y)])
    # 시작점 방문 처리
    graph[x][y] = 1

    while q:
        # 큐에서 현재 노드 가져옴
        x, y = q.popleft()

        # 상하좌우 네 방향에 대해서 반복
        for i in range(4):
            # 방향별로 인접한 노드의 좌표계산
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프 범위를 벗어나지 않으면서, 구멍칸 및 방문하지 않은 칸 인경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                # 인접 노드 큐에 추가하고 방문 처리
                q.append((nx, ny))
                graph[nx][ny] = 1

    # 참을 반환하여 칸을 채웠음을 알림
    return True

# 열과 행 개수 입력 받음
n, m = map(int, input().split())
# 2차원 리스트 초기화
graph = []
# 결과 값 초기화
result = 0

# n열 만큼 반복 입력 받는다
for _ in range(n):
    graph.append(list(map(int, input())))

# 좌표 하나하나에 대해서 탐색 실시한다
for i in range(n):
    for j in range(m):
        # 채우기가 실행 되었다면 결과 값 증가
        if dfs(i, j) == True:
        # if bfs(i, j) == True:
            result += 1

# 결과 출력
print(result)