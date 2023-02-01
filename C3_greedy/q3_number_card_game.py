# 행과 열 수를 입력 받음
n, m = map(int, input().split())

# 최소값을 담을 결과 값 초기화
result = 0

# 행 마다 반복문 실행  
for i in range(n):
    # 행 데이터 입력 받음
    data = list(map(int, input().split()))
    # 행에서 최소값 선택
    min_val = min(data)
    # 행의 최솟값 중에서 제일 큰 값을 선택
    result = max(result, min_val)

# 결과 출력
print(result)