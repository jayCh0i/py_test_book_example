# 창고들을 하나 건너서 털 수 밖에 없기 때문에 점화식은 두 단계 전 까지만 고려하면 된다.
## 이전 창고(i-1)를 털었던 경우에는 현재 창고는 털지 못하고 넘어간다.
## 전의전 창고(i-2)를 털었던 경우에는 현재 창고를 털 수 있다.
## 그 이전에서의 값들은 이미 최적값으로 고려되어 있으므로 i-2까지만 비교하여 더 높은 값을 취한다.

# 정수 입력 받음
n = int(input())
# 창고 정보를 리스트로 묶어서 받는다
array = list(map(int, input().split()))

# DP 테이블 초기화
dp_table = [0] * (n+1)
# 반복 문제에서 벗어나는 예외 단계는 직접 입력
dp_table[0] = array[0]
dp_table[1] = max(array[0], array[1])

# 점화식 구현
for i in range(2, n):
    dp_table[i] = max(dp_table[i-1], dp_table[i-2] + array[i])

# 결과 출력
print(dp_table[n-1])