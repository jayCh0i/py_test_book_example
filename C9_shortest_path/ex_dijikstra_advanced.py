# 기존 다익스트라 알고리즘에서 제일 짧은 거리의 노드를 찾기 위한 반복문의 시간 복잡도 문제를
# 힙큐(heap queue)를 활용하여 개선시킨 버전이다.
## 시작점에서 부터 연결된 가까운 노드부터 계산되어 나가는 특성상
## 한 노드의 최단 거리값은 노드가 선택되기 이전에 완성되며, 선택되고 나면 줄어들지 않는다는 특징이 있다

import sys, heapq

# 입력 문자수가 많아질수 있기때문에 기본 input()말고 readline() 사용
input = sys.stdin.readline
# 무한대 값으로 대신 사용할 상수 선언
INF = int(1e9)

def do_dijikstra_advanced(start):
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
        if distance[now] < dist :
            continue

        # 해당 노드와 인접한 노드들을 처리, 데이터 순서에 주의(노드 번호, 간선 거리)
        for i in graph[now]:
            # 현재 노드를 거쳐 가는것이 더 짧을 때만 갱신
            new_dist = distance[now] + i[1]

            if new_dist < distance[i[0]]:
                distance[i[0]] = new_dist
                heapq.heappush(q, (new_dist, i[0]))

    # 결과 출력
    for i in range(1, v+1):
        if distance[i] == INF:
            print('Cannot reach')
        else:
            print(distance[i])


# 노드와 간선 수 입력 받음
v, e = map(int, input().split())
# 시작점 입력 받음
start = int(input())

# 노드별 간선 그래프 초기화
graph = [[] for i in range(v+1)]
# 최단 거리 테이블, 모두 기본값을 무한으로 초기화
distance = [INF] * (v+1)

# 간선 개수 만큼 입력 받음
for _ in range(e):
    a, b, dist = map(int, input().split())
    # (연결노드, 비용)형태의 튜플로 추가
    graph[a].append((b, dist))

do_dijikstra_advanced(start)