# 변수 입력 받읍
n, k = map(int, input().split())
# 결과값 변수 초기화
result = 0

while True :
    # 현재 n 이하의 가장 가까운 k의 배수를 구한다
    target = (n // k) * k
    # 가장 가까운 K의 배수까지 1을 빼야하는 횟수를 더함
    result += (n - target)
    
    # 더 이상 나눌 수 없는 경우 종료
    if n < k:
        break
    # k로 나눈다
    n //= k
    result += 1

# 남은 수가 1이 될때까지 1을 빼야하는 횟수만큼 더하기
result += (n-1)

# 결과 출력
print(result)