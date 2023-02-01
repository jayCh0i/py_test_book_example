# 총 인원 수 입력 받음
n = int(input())
# 인원 리스트 입력 받음
array = list(map(int, input().split()))
# 결과값 변수 초기화
result = 0
# 현재 그룹에 포함 된 인원수를 저장할 변수 초기화
count = 0

# 배열 오름차순 정렬
array.sort()

# n부터 0 까지 반복
for i in array:
    # 현재 모험가를 그룹에 추가
    count += 1
    # 현재 모험가의 공포도를 만족하는 인원이 모였을때 그룹 결성
    if count >= i:
        result += 1
        count = 0

# 결과 출력
print(result)