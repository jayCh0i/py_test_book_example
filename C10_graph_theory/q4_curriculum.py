from collections import deque
import copy

def do_topology():
    q = deque()
    # 결과 값 리스트. 강의 별 초기값도 필요하므로 리스트를 복사한다.
    ## 리스트의 하위 요소들이 복사 되지않고 주소를 공유하는
    ## 문제가 생길수 있으므로 깊은복사로 복사해야 완벽하게 복사할 수 있다
    total_time = copy.deepcopy(time)

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        ### test case1
        ## 4
        ## 30 -1
        ## 20 -1
        ## 40
        ## > 30 20 70

        # now: 현재 강의(선수 강의), i: 연결된 강의(현재 강의을 선행해야 들을 수 있는 강의)
        for i in graph[now]:
            # 연결된 강의의 진입 차수 감소
            indegree[i] -= 1
            # 선수 강의(now)과 연결 강의(i)의 강의 시간을 더해서 연결 강의의 총 강의 시간을 기록
            # > max() 비교는 왜 했을까?
            ## 한 강의에 선행 강의가 다수 있을때, 이를 동시에 수강한다고 가정되어있다.
            ## 이런 경우 "제일 긴 강의"만큼의 시간이 걸리므로
            ## 제일 긴 선행 강의와 합산된 값을 선택하기 위해 max() 비교를 진행한다.
            total_time[i] = max(total_time[i], total_time[now] + time[i])

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v+1):
        print(total_time[i], end=' ')

# 노드와 간선 개수 입력받음
v = int(input())
# 위상정렬 알고리즘을 위한 그래프 리스트
graph = [[] for i in range(v+1)]
# 위상정렬 알고리즘을 위한 진입차수 리스트
indegree = [0] * (v+1)
# 강의 시간 정보 리스트
time = [0] * (v+1)

# 노드 개수 만큼 입력 받음
for i in range(1, v+1):
    # 리스트 형식으로 입력받음
    ## [강의시간, 복수개의 선수강의들..., -1]
    data = list(map(int, input().split()))

    # 우선 자기 강의 시간만큼의 시간만큼 지정
    time[i] = data[0]

    for j in data[1:-1]:
        # 선수 강의에 간선 기록 (선수강의에서 -> 현재강의으로)
        graph[j].append(i)
        # 현재 강의의 진입 차수 증가
        indegree[i] += 1

do_topology()