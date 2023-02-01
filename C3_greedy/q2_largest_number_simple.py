# 기본 변수를 입력 받음
n, m, k = map(int, input().split())
# 숫자 배열을 입력 받음
data = list(map(int, input().split()))

# 배열 오름차순 정렬
data.sort()

# 최대값을 만들기 위해 제일 큰 수 두개를 고른다
first = data[n-1]
second = data[n-2]

# 결과 값 초기화
result = 0

while True:
    # 제일 큰 수를 k번 더한다
    for i in range(k):
        # 남은 횟수가 0일 경우 반복 종료
        if m < 1 :
            break;
        # 횟수가 남아있다면 첫 번째로 큰 수를 결과값에 추가하고 횟수 1 차감
        result += first
        m -= 1
    
    # 남은 횟수가 0일 경우 반복 종료
    if m < 1 :
        break;
    # 아직 횟수가 남아있다면 두 번째로 큰 수를 결과값에 1회 추가하고 횟수 1 차감
    result += second
    m -= 1

# 결과 출력
print(result)