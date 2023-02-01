import sys

input = sys.stdin.readline

# 순차 탐색
def sequential_search(n, array, target):
    # 일일이 돌리면서 탐색한다
    for i in range(n):
        # 찾은경우
        if array[n] == target:
            # +1을 하여 순서를 반환
            return i+1

    # 끝까지 찾지 못한경우
    return None


# 재귀 함수 방식의 이진 탐색
def bin_search_recursive(array, target, start, end):
    # 끝까지 찾지 못한경우
    if start > end:
        return None

    # 중간 값을 구한다.
    mid = (start + end) // 2

    if array[mid] == target: # 찾은 경우
        return mid
    elif array[mid] > target:
        # 검색값(target)이 더 작은 경우, 끝 값을 중간 값 이전까지 줄인다.
        return bin_search_recursive(array, target, start, mid-1)
    else: 
        # 검색값(target)이 더 큰 경우, 시작 값을 중간 값 다음까지 늘린다.
        return bin_search_recursive(array, target, mid+1, end)

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

# 원소 개수와 검색할 값 입력
n, target = map(int, input().split())
# 전체 원소 입력 받기
array = list(map(int, input().split()))

res = bin_search_loop(array, target, 0, n-1)
print("4: ","Not found" if res == None else res+1 )