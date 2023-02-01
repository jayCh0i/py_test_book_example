# 파이썬의 간결한 문법을 활용하여 간단하게 만든 퀵 정렬 코드
## 코드는 간단하지만 원소들의 위치를 바꾸는 과정대신
## 피봇값을 기준으로 반으로 나누기 때문에 연산 횟수가 증가하는 단점이 있다.

def quick_sort_short(array):
    # 리스트 원소개수가 1개 이하인 경우 종료
    if len(array) <= 1:
        return array

    # 피봇으로 첫 원소값 지정
    pivot = array[0]
    # 피봇을 떼어낸 리스트 생성
    tail = array[1:]

    # 피봇값을 기준으로 왼쪽, 오른쪽 부분으로 나눈다
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    # 왼쪽, 오른쪽 부분도 정렬을 진행, 피봇을 포함하여 합친뒤 전체 리스트를 반환
    return quick_sort_short(left_side) + [pivot] + quick_sort_short(right_side)
    

# 리스트 데이터 입력 받음
array = list(map(int, input().split()))

# 결과 출력
print(quick_sort_short(array))