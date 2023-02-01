# 변수 입력 받읍
n, k = map(int, input().split())
# 결과값 변수 초기화
result = 0

# n이 k보다 작아져서 나누지 못할 때까지 반복
while n >= k :
    # n이 k로 나누어 떨어지지 않는다면 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # k로 나누기
    n //= k
    result += 1

# 남은 수가 1이 될때까지 1을 차감하는 횟수만큼 더하기
result += (n-1)

# 결과 출력
print(result)