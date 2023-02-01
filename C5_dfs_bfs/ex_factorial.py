# 반복문 방식의 팩토리얼
def factorial_iteration(n):
    result = 1

    # 팩토리얼은 n까지의 모든 정수의 곱이다
    for i in range(1, n+1):
        result *= i

    return result

# 재귀 함수 방식의 팩토리얼
def factorial_recursive(n):
    # 1일 경우에는 1을 반환후 종료
    if n <=1:
        return 1

    # 재귀를 통한 팩토리얼의 점화식 구현
    return n * factorial_recursive(n-1)

print('iteration: ', factorial_iteration(5))
print('recursive: ', factorial_recursive(5))