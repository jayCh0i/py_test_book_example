# 무한대 값으로 대신 사용할 상수 선언
INF = int(1e9)

def do_floyd_warshall():
    # 경유지와 도착지 입력 받음
    x, k = map(int, input().split())

    # 바로 가는것과 경유지를 거쳐가는 경우 중 더 짧은 경로를 선택한다
    # 모든 경유지의 경우을 계산해야 하므로, '경유지'를 기준으로 3중 반복문을 통해 알고리즘을 수행한다
    for mid in range(1, v+1):
        for start in range(1, v+1):
            for end in range(1, v+1):
                # 점화식 사용
                graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

    # 결과 출력
    result = graph[1][k] + graph[k][x]
    if result >= INF:
        print(-1)
    else:
        print(result)

# 노드와 간선 수 입력 받음
v,e = map(int, input().split())
# 노드별 간선 그래프 초기화
## 모든 노드에서 다른 모든 노드로의 거리를 저장해야 하므로 2차원 배열을 사용한다.
graph = [[INF] * (v+1) for _ in range(v+1)]

# 자기 자신으로 향하는 거리 값은 0으로 초기화
for i in range(v+1):
    graph[i][i] = 0

# 도시 사이는 거리가 1이고 양방향 이동 가능이므로, 양쪽 노드에 거리 1의 간선을 기록
for _ in range(e):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

do_floyd_warshall()