# 한 출발지점에서 다른 각각의 노드에 대한 최단 경로를 구하는 알고리즘
# 가장 적은 비용의 노드를 선택해서 이를 반복하는 구조라 그리디 알고리즘으로 분류된다.
## 시작점에서 부터 연결된 가까운 노드부터 계산되어 나가는 특성상
## 한 노드의 최단 거리값은 노드가 선택되기 이전에 완성되며, 선택되고 나면 줄어들지 않는다는 특징이 있다

import sys
# 입력 문자수가 많아질수 있기때문에 기본 input()말고 readline() 사용
input = sys.stdin.readline
# 무한대 값으로 대신 사용할 상수 선언
INF = int(1e9)

# 미방문 노드중, 최단 거리의 노드 인덱스를 검색
def get_smallest_node():
    min_val = INF
    index = 0

    # 노드 개수 만큼 단순 반복, 이것이 속도 저하의 주 요인
    for i in range(1, v+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i

    return index

def do_dijikstra_basic(start):
    # 시작 노드에 대한 초기화 진행
    distance[start] = 0
    visited[start] = True
    # 시작 노드에 연결된 노드들의 최단거리 갱신
    for i in graph[start]:
        distance[i[0]] = i[1]
    
    # 시작 노드를 제외한 노드 개수만큼 반복
    for i in range(v-1): 
        # 시작 노드 다음으로 작은 미방문한 노드부터 진행
        now = get_smallest_node()
        # 현재 노드 방문처리
        visited[now] = True

        # 해당 노드와 인접한 노드들을 처리
        for j in graph[now]:
            # 현재 노드를 거쳐 가는것이 더 짧을 때만 갱신
            new_dist = distance[now] + j[1]

            if new_dist < distance[j[0]]:
                distance[j[0]] = new_dist

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
# 노드별 방문 기록 리스트 초기화
visited = [False] * (v+1)
# 최단 거리 테이블, 모두 기본값을 무한으로 초기화
distance = [INF] * (v+1)

# 간선 개수 만큼 입력 받음
for _ in range(e):
    a, b, dist = map(int, input().split())
    # (연결노드, 비용)형태의 튜플로 추가
    graph[a].append((b, dist))

do_dijikstra_basic(start)