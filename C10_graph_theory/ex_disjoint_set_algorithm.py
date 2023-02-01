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
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

# 노드와 간선 개수 입력
v, e = map(int, input().split())
# 부모 테이블
parent = [0] * (v+1)

# 자신의 노드 번호 값으로 부모 테이블 초기화
for i in range(1, v+1):
    parent[i] = i

# 간선 개수 만큼 입력 받음
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

    print("각 원소가 속한 집합 출력: ", end='')
    for i in range(1, v+1):
        print(find_parent(parent, i), end=" ")
    
    print()

    print('부모 테이블 : ', end='')
    for i in range(1, v+1):
        print(parent[i], end=' ')
