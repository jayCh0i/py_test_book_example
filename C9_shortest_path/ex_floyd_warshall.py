# 모든 지점에서 다른 모든 지점까지의 최단 경로를 구하는 알고리즘
# 점화식을 사용하는 특성상 다이나믹 프로그래밍 알고리즘으로 분류된다.
## 반복문마다 한 경유지를 기준으로 지나가는 모든 경로를 고려해서
## 곧 바로 가는것과 경유해서 가는것을 비교하여 최단 경로를 갱신한다.

# 무한대 값으로 대신 사용할 상수 선언
INF = int(1e9)

def do_floyd_warshall():
    # 바로 가는것과 경유지를 거쳐가는 경우 중 더 짧은 경로를 선택한다
    # 모든 경유지의 경우을 계산해야 하므로, '경유지'를 기준으로 3중 반복문을 통해 알고리즘을 수행한다
    for mid in range(1, v+1):
        for start in range(1, v+1):
            for end in range(1, v+1):
                # 점화식 사용
                graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

    # 결과 출력
    for start in range(1, v+1):
        for end in range(1, v+1):
            if graph[start][end] == INF :
                print("INF", end=' ')
            else:
                print(graph[start][end], end=' ')
        print()

# 노드와 간선 수 입력 받음
v = int(input())
e = int(input())

# 노드별 간선 그래프 초기화
## 모든 노드에서 다른 모든 노드로의 거리를 저장해야 하므로 2차원 배열을 사용한다.
graph = [[INF] * (v+1) for _ in range(v+1)]

# 자기 자신으로 향하는 거리 값은 0으로 초기화
for i in range(1, v+1):
    graph[i][i] = 0

# 간선 개수 만큼 입력 받음
for _ in range(e):
    a, b, dist = map(int, input().split())
    graph[a][b] = dist

do_floyd_warshall()