# 정수 개수 입력 받음
n = int(input())
# 입력 정수 리스트 초기화
array = []

# n개의 정수 입력 받음
for _ in range(n):
    array.append(int(input()))

# 기본 라이브러리를 사용해 내림차순 정렬 진행
array.sort(reverse=True)

# 결과 출력
for i in array:
    print(i, end=' ')

