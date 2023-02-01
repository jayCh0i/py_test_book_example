# 변수 입력 받음
n, m = map(int, input().split())
# 리스트 입력 받음
array = list(map(int, input().split()))

# 1 ~ m까지의 무게별로 개수를 저장할 배열 초기화
count = [0] * m
# 결과값 초기화
result = 0

# 무게별로 개수를 기록
for i in array:
    count[i] += 1

# 무게 1부터 m까지 반복
for i in range(1, m+1):
    # 전체 개수에서 현재 무게의 공 개수만큼을 빼면 현재 무게보다 무거운 공들의 개수만 남는다.
    n -= count[i]
    # 경우의 수를 기록
    result += count[i] * n

# 결과 출력
print(result)