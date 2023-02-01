# 노드 소속 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 노드 병합
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def do_kruskal(parent):
    # 총 간선 비용
    total_cost = 0
    # 제일 큰 간선 비용
    largest_cost = 0

    # 크루스칼 알고리즘 실시
    for edge in edges: 
        # 튜플의 데이터 순서 유의
        cost, a, b = edge

        # 두 노드끼리 싸이클이 발생하지 않은 경우에만 노드 연결
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total_cost += cost
            # 제일 큰 간선 비용 갱신
            ## 노선 정보 테이블이 비용의 오름차순으로 정렬되어
            ## 마지막에 처리되는 노선의 비용이 제일크다
            largest_cost = cost
        
    # 마지막에 처리되는 간선이 빠지게 되면
    # 2개로 신장 트리로 분할 되면서, 최소 비용을 만족하게 된다.
    print(total_cost - largest_cost)

# 노드와 간선 개수 입력
v, e = map(int, input().split())
# 부모 테이블
parent = [0] * (v+1)
# 노선 정보
edges = []

# 자신의 노드 번호 값으로 부모 테이블 초기화
for i in range(1, v+1):
    parent[i] = i

# 간선 개수 만큼 입력 받음
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 간선을 비용 기준으로 정렬하기 위해 튜플의 첫 값을 비용으로 함
    edges.append((cost, a, b))

# 첫 키값(비용)을 기준으로 오름차순 정렬
edges.sort()

do_kruskal(parent)
