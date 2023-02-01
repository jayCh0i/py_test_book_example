# 위상 정렬 알고리즘은 순서나 방향이 있는 상태에서
# 이를 거스르지 않고 모든 노드들을 나열하기 위한 알고리즘의 한 종류이다.
# - 방향성 그래프에 적용되며, 진입차수 개념을 사용한다.

from collections import deque

def do_topology() :
    # 힙큐 생성
    q = deque()
    # 정렬 순서를 담는 결과값 리스트
    order_result = []

    # 제일 먼저 진입차수 0인 노드부터 시작
    for i in range(1, v+1):
        if indegree[i] == 0 :
            q.append(i)

    while q:
        now = q.popleft()
        # 처리 당하는 노드를 결과값에 기록
        order_result.append(now)

        # 연결된 노드의 진입차수 1감소
        for i in graph[now]:
            indegree[i] -= 1
            # 진입차수 계산후 0이 된다면 큐에 넣기
            if indegree[i] == 0 :
                q.append(i)

    # 결과 출력
    for i in order_result:
        print(i, end=' ')

# 노드와 간선 개수 입력받음
v, e = map(int, input().split())
# 노드별 진입 차수
indegree = [0] * (v+1)
# 노드별 간선 그래프 초기화
graph = [[] for i in range(v+1)]

# 간선 개수 만큼 입력 받음
for _ in range(e):
    a, b = map(int, input().split())

    # 노드 정보 입력
    graph[a].append(b)
    # 도착 노드에 진입차수 1증가
    indegree[b] += 1

do_topology()