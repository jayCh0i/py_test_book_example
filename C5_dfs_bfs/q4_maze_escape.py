# 시작점에서 상하좌우 방문하지 않은 인접 노드에 대해 탐색을 하면서
# 노드 별로 이동 횟수 데이터를 기록하면서 도착지점 까지 탐색을 완료하면 된다.
## 입력받는 그래프 데이터가 인접 리스트 형식이 아니라 단순 2차원 리스트로만 주어지기 때문에,
## 한 칸 옆에 인접해 있는 노드들을 처리하려면 직접 좌표값을 계산해서 다음 연산으로 이어가야 한다
### 방문 여부 및 최단 거리값은 그래프 리스트의 원소 값을 이용하면 된다.

from collections import deque

# 1칸 인접한 노드들의 좌표를 계산하기 위한 변수 선언(상하좌우 순서)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    ## 갈수 없는 공간이라면 중지, 단 문제 조건에 시작점 (1,1) 은 항상 1이므로 생략
    # if graph[x][y] == 0:
    #     return False

    # 큐로 사용할 리스트 선언과 동시에 시작점를 첫 원소로 추가한다.
    q = deque([(x,y)])

    while q:
        # 큐에서 현재 노드 가져옴
        x, y = q.popleft()

        # 상하좌우 네 방향에 대해서 반복
        for i in range(4):
            # 방향별로 인접한 노드의 좌표계산
            nx = x + dx[i]
            ny = y + dy[i]

            # 그래프 범위를 벗어나지 않으면서, 방문하지 않은 칸 인경우
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                # 인접 노드 큐에 추가하고 방문 처리
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

# 열과 행 개수 입력 받음
n, m = map(int, input().split())
# 2차원 리스트 초기화
graph = []

# n열 만큼 반복 입력 받는다
for _ in range(n):
    graph.append(list(map(int, input())))

# (1,1) 부터 탐색 실시
bfs(0,0)

# (n,m) 최단 거리 결과 출력
print(graph[n-1][m-1])