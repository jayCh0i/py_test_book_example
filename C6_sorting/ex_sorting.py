# 제일 기본적인 선택정렬, 하나씩 선택하여 정렬을 한다고하여 선택 정렬이라고 부른다
# 배열에서 가장 작은 값을 하나 선택해서 앞에 두는 것을 반복한다.
## 2중 반복문이 거의 매번 돌아가기 때문에 매우 비효율적이다.
def selection_sort():
    array = list(map(int, input().split()))

    for i in range(len(array)):
        # 가장 작은 값의 인덱스를 찾을 변수
        cursor = i
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                pointer = j
        # 서로의 값을 스와핑 시킨다
        array[i], array[cursor] = array[cursor], array[i]

    #결과 출력
    print(array)

# 데이터를 하나씩 확인하면서 정렬이 필요할때만 위치 교환을 진행한다
# 첫 번째 데이터는 정렬된 데이터로 가정하고 다음 데이터 부터 정렬된 데이터와 비교를 한다.
## 필요할때만 정렬을 하기때문에 거의 정렬된 데이터를 정렬할때 매우 효율적이며
## 정렬된 데이터는 자동으로 오름차순을 유지하는 특성이 있다.
def insertion_sort():
    array = list(map(int, input().split()))

    for i in range(len(array)):
        # 작동 점위는 i 부터 1까지 정렬된 데이터들의 범위 만큼, 역순(-1)으로 진행한다
        for j in range(i, 0, -1):
            # 자기보다 작은 값이 나올때 까지 한 칸씩 왼쪽으로 이동한다.
            if array[j] < array[j-1]:
                 array[j], array[j-1] = array[j-1], array[j]
            else:
                # 자기보다 작은 값을 만나면 멈춤
                break

    print(array)
