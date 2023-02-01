# 기본 변수를 입력 받음
n, m, k = map(int, input().split())
# 숫자 배열을 입력 받음
data = list(map(int, input().split()))

# 배열 오름차순 정렬
data.sort()

# 최대값을 만들기 위해 제일 큰 수 두개를 고른다
first = data[n-1]
second = data[n-2]

# 제일 큰수를 k회 반복하고 두번째 큰수를 한번 더한 패턴이 가능한 만큼의 합
pattern_summary = (first * k + second) * (m // (k+1))
# 패턴 계산 후 남은 횟수를 제일 큰 수로 더한 합
other_summary = (first * (m % (k+1)))

# 결과 출력
print(pattern_summary + other_summary)