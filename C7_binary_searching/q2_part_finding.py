import sys

input = sys.stdin.readline

# 반복문 방식의 이진 탐색
def bin_search_loop(array, target, start, end):
    # 찾을게 있을때 까지
    while start <= end:
        # 중간 값을 구한다.
        mid = (start + end) // 2

        if array[mid] == target: # 찾은 경우
            return mid
        elif array[mid] > target:
            # 검색값(target)이 더 작은 경우, 끝 값을 중간 값 이전까지 줄인다.
            end = mid -1
        else:
            # 검색값(target)이 더 큰 경우, 시작 값을 중간 값 다음까지 늘린다.
            start = mid +1
            
    # 끝까지 찾지 못한 경우
    return None

# 이진 탐색을 통한 부품 검색
def find_part():
    # 재고 부품 개수 입력
    n = int(input())
    # 재고 부품 리스트 입력
    stocks = list(map(int, input().split()))

    # 필요 부품 개수 입력
    m = int(input())
    # 필요 부품 리스트 입력
    targets = list(map(int, input().split()))

    # 필요 부품 별로 이진 검색 실행
    for _ in range(m):
        result = bin_search_loop(stocks, targets[m], 0, n-1)

        # 결과 출력
        if result != None:
            print('yes', end=' ')
        else:
            print('no', end=' ')

# 중복 데이터가 제거되는 집합 자료형인 set을 통한 간결한 부품 검색
def find_part_by_set():
    # 재고 부품 개수 입력
    n = int(input())
    # set을 활용한 재고 부품 리스트 입력
    stocks = set(map(int, input().split()))

    # 필요 부품 개수 입력
    m = int(input())
    # 필요 부품 리스트 입력
    targets = list(map(int, input().split()))

    # 필요 부품 별로 검색 실행
    for target in targets:
        # 결과 출력
        ## 집합 자료형의 데이터들은 중복이 제거되기 때문에 간단하게 검색만 해도 된다
        if target in stocks:
            print('yes', end=' ')
        else:
            print('no', end=' ')


find_part()
