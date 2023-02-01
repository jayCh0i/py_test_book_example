# 퀵 정렬은 대부분의 상황에서 빠른 성능을 보장되어 두루 사용되는 알고리즘이다.
# 피벗이라는 기준값을 잡고 큰수와 작은수를 교환하고 반으로 분할하고 이를 반복해나간다.
## 피벗보다 큰 수는 왼쪽에서부터 찾고, 피벗보다 작은 수는 오른쪽에서 부터 찾아나간다.
## 아래 코드는 호어 분할 방식을 기준으로 작성되었다.

def quick_sort(array, start, end):
    # 원소가 1개인 경우 정렬 종료
    if start >= end:
        return

    # 피벗값은 첫번째 원소로 시작한다
    pivot = start

    # 왼쪽 오른쪽 값 초기화
    left = start + 1
    right = end

    # 왼쪽과 오른쪽이 교차하는 시점이 분할할 시점
    while left <= right:
        # 왼쪽에선 피벗값 보다 큰 값을 발견할 때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 오른쪽에선 피벗값 보다 작은 값을르 발견할 때 까지 반복
        ## start는 피봇이므로 start 보다 클때 까지만 반복하도록 한다
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            # 서로 교차했다면 작은 데이터(오른쪽 값)을 피벗과 교체하고 반복 종료
            array[right], array[pivot] = array[pivot], array[right]
        else:
            # 엇갈리지 않았다면 왼쪽과 오른쪽 값을 서로 교체하고 반복 재개
            array[left], array[right] = array[right], array[left]

    # 왼쪽과 오른쪽으로 분할해서 각각 정렬을 수행시킨다.
    ## 오른쪽 값이 피봇으로 교체 되었으므로 오른쪽 기준으로 분할한다.
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


# 리스트 데이터 입력 받음
array = list(map(int, input().split()))

quick_sort(array, 0, len(array)-1)

# 결과 출력
print(array)