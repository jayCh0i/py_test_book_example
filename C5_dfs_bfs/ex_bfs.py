# BFS(너비 우선 탐색)는 큐를 사용하는 가장 가까운 노드부터 탐색하는 알고리즘이다.
# 일반적으로 DFS 보다 BFS가 시간 효율이 좋은 편이다.
## 진행 과정이 시작점을 중심으로 퍼져나가는 모양새로 진행된다.
### 작동 방식이 노드에 연결된 모든 인접 노드들을 확인 해봐야므로 '인접 리스트' 방식이 적합하다

from collections import deque

def bfs(graph, start, visited):
    # 큐로 사용할 리스트 선언과 동시에 시작점를 첫 원소로 추가한다.
    q = deque([start])
    # 시작점 방문 처리
    visited[start] = True

    # 큐가 빌때까지 반복
    while q:
        # 큐에서 현재 노드 가져옴
        now = q.popleft()
        # 현재 처리중인 노드 출력
        print(now, end=' ')

        for i in graph[now]:
            # 인접 노드가 방문하지 않은 경우에 계속 진행
            if not visited[i]:
                # 큐에 추가하고 방문 처리
                q.append(i)
                visited[i] = True

# 노드 연결 정보를 담은 인접 리스트 선언
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]
# 노드 방문 정보 리스트 초기화
visited = [False] * 9

# BFS 실행
bfs(graph, 1, visited)