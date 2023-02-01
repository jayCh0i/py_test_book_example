# 주어진 데이터가 매우 큰 정수가 주어진것으로 이진 탐색이라는것을 짐작하자
# 이진 탐색 문제이면서 파라메트릭 서치 유형의 문제이다
## 파라메트릭 서치는 최적의 해를 찾는 문제를
## 예/아니요로 판별되는 '결정 문제'로 전환하여 해결하는 기법이다.
### 이 값으로 조건을 만족하는가? > 예/아니오 > 범위 조정 과정을 거치는데
### 이 범위를 좁히는 과정에서 이분 탐색을 적용할 수 있겠다

import sys

# 대량의 데이터를 빠르게 입력 받기 위한 readline 함수를 변수으로 지정해둔다
input = sys.stdin.readline

# 떡의 개수와 원하는 떡의 길이를 입력 받음
n, m = map(int, input().split())
# 떡의 개별 높이를 입력 받음
array = list(map(int, input().split()))

# 이진 탐색 처음 값 초기화
start = 0
# 이진 탐색 끝 값 초기화
end = max(array)

# 결과 값 변수 초기화
result = 0

# 이진 탐색을 진행
while start <= end:
    # 자른 떡들의 길이를 담을 변수 초기화
    total = 0
    # 중간 값
    mid = (start+end) // 2

    # 중간 값을 대보고 잘릴 떡의 길이를 구함
    for i in array:
        if i > mid:
            total += i - mid
    
    # 잘린 떡이 부족 할때, 절단 높이를 낮춘다
    if total < m:
        end = mid -1
    # 잘린 떡이 충분할 때, "현재 높이를 기록하고" 절단 높이를 높힌다
    else:
        start = mid + 1
        # 결과값 갱신
        ## 요구하는 떡의 길이는 모자란건 안되도 더 긴 것은 되기에
        ## 이것을 충족하는 마지막 값이 결과값이라 할 수 있다.
        result = mid

# 결과 출력
print(result)
