# 문자열 입력 받음
str = input()

# 문자열의 첫번째 숫자로 결과값을 초기화
result = int(str[0])

# 두번째 숫자부터 반복 시작
for i in range(1, len(str)):
    current = int(str[i])

    # 결과값과 현재값이 1 이하인 경우 더한다.
    if result <= 1 or current <= 1:
        result += current
    else:
        # 그외 경우에는 현재값을 곱한다
        result *= current

# 결과 출력
print(result)
