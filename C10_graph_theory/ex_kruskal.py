# 크루스칼 알고리즘은 최소 비용으로 모든 노드를 연결하기 위한
# 최소 신장 알고리즘의 한 종류이다
# - 무방향성 그래프에 적용되며, 서로소 집합 자료구조를 활용한다

# 노드 소속 집합 찾기
def find_parent(parent, x):
    if parent[x] != x :
        # 재귀 결과값으로 부모값을 변경하면서 경로 압축 진행
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 노드 병합
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 트리구조 원리상 노드가 더 작은것이 부모 노드가 된다
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

def do_kruskal(parent):
    # 총 비용
    total_cost = 0

    # 크루스칼 알고리즘 실시
    for edge in edges:
        # 튜플의 데이터 순서 유의
        cost, a, b = edge

        # 두 노드끼리 싸이클이 발생하지 않은 경우에만 노드 연결
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total_cost += cost

    print(total_cost)

# 노드와 간선 개수 입력
v, e = map(int, input().split())
# 부모 테이블
parent = [0] * (v+1)
# 노선 정보
edges = []

# 자신의 노드 번호 값으로 부모 테이블 초기화
for i in range(1, v+1):
    parent[i] = i

# 간선 개수 만큼 정보 입력 받음
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 간선을 비용 기준으로 정렬하기 위해 튜플의 첫 값을 비용으로 함
    edges.append((cost, a, b))

# 첫 원소값인 cost 기준으로 오름차순 정렬
edges.sort()

do_kruskal(parent)

