# 정수 입력 받음
n = int(input())

# DP 테이블 초기화
dp_table = [0] * (n+1)

# 각 연산 별로 점화식을 작성해서 가장 작은 값을 얻을 수 있도록 한다.
## 점화식에서 현재 연산의 횟수26를 포함하기 위해 1을 더한다.
for i in range(2, n+1):
    # 모든 수에 적용되는 1을 빼는 경우의 점화식.
    dp_table[i] = dp_table[i-1] + 1

    # 2로 나누어 떨어지는 경우의 점화식. 위의 점화식의 결과와 비교하여 더 작은값을 선택한다.
    if i % 2 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i//2] + 1)

    # 3로 나누어 떨어지는 경우의 점화식. 동일하게 진행한다.
    if i % 3 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i//3] + 1)

    # 5로 나누어 떨어지는 경우의 점화식. 동일하게 진행한다.
    if i % 5 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i//5] + 1)

# 결과 출력
print(dp_table[n])