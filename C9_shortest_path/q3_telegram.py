import heapq

# 무한대 값으로 대신 사용할 상수 선언
INF = int(1e9)

def do_dijikstra(start):
    # 힙큐로 사용할 리스트 선언, (최단 거리, 노드번호) 구조의 튜플을 사용
    ## 파이썬 힙큐는 최소힙의 구조를 가져 최소값의 원소부터 반환하며
    ## 기본적으로 데이터의 첫번째 원소를 기준으로 정렬한다.
    q = []

    # 시작 노드에 대한 초기화 진행
    distance[start] = 0
    # 시작 노드의 정보를 힙큐에 추가
    heapq.heappush(q, (0, start))

    while q:
        # 최소 거리의 노드를 추출
        dist, now = heapq.heappop(q)

        # 노드의 최단 거리값은 노드가 선택되기 이전에 완성되기 때문에
        # 선택된 상태에서 힙큐에서 가져온 최단 거리보다 최단 거리 테이블 값이 더 작다면
        # 이미 처리 노드이며 이 경우에는 무시하고 넘어간다.
        if distance[now] < dist:
            continue

        # 해당 노드와 인접한 노드들을 처리, 데이터 순서에 주의(노드 번호, 간선 거리)
        for i in graph[now]:
            # 현재 노드를 거쳐 가는것이 더 짧을 때만 갱신
            new_dist = distance[now] + i[1]

            if new_dist < distance[i[0]]:
                distance[i[0]] = new_dist
                heapq.heappush(q, (new_dist, i[0]))

        # 도달 가능한 노드 수와, 제일 먼 거리값 변수 초기화
        count, max_distance = 0, 0

        # 결과 계산
        for dist in distance:
            if dist != INF:
                count += 1
                max_distance = max(max_distance, dist)

        # 결과 출력, count에서 시작 노드는 제외한다
        print(count-1, max_distance)

# 노드와 간선 수, 시작점 입력 받음
v,e, start = map(int, input().split())

# 노드별 간선 그래프 초기화
graph = [[] for i in range(v+1)]
# 최단 거리 테이블, 모두 기본값을 무한으로 초기화
distance = [INF] * (v+1)

# 간선 개수 만큼 입력 받음
for _ in range(e):
    a, b, dist = map(int, input().split())
    # (연결노드, 비용)형태의 튜플로 추가
    graph[a].append((b, dist))

do_dijikstra(start)