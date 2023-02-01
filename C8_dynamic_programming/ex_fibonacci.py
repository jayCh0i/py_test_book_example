# 다이나믹 프로그래밍은 큰 문제를 반복되는 작은 문제로 나누고
# 같은 문제라면 한번씩만 풀어도 되도록 하여 문제를 효율적으로 해결하는 알고리즘이다.
## 큰 문제에서 작은 문제를 호출해 나가면 '탑 다운/하향식' 방식이라고 하며
## 큰 문제부터 해결하기 위해 주로 재귀함수를 이용한다.
## 여기서 단계별 결과값을 저장하여 중복 연산을 줄이는 기법을 메모이제이션(메모화)이라고 한다.
### 반대로 작은 문제부터 구하면서 마지막에 큰 문제를 해결하는 방식을 '보텀 업/상향식' 방식이라고 하며
### 주로 반복문을 이용하여 아래부터 위로 올라간다.
#### 재귀함수가 커지면 시스템의 함수 호출 스택에 오버플로우를 일으킬 수 있으므로
#### 하향식 재귀함수를 먼저 작성해보고 상향식 반복문으로 변경 가능하다면 수정 하는것이 좋다.

# 기본적인 재귀함수를 통한 피보나치 배열
## 재귀 함수가 매번 계산을 해야 하기 때문에 비효율적이다.
def fibo_basic(x):
    if x == 1 or x == 2:
        return 1
    # 재귀 피보나치 연산을 수행, 
    else:
        return fibo_basic(x-1) + fibo_basic(x-2)

# 메모이제이션 기법을 추가한 재귀 피보나치 배열 함수
## 한번 수행된 결과는 리스트에 저장하여 재사용하기 때문에 반복 횟수가 크게 줄어든다.
# 결과 값을 저장할 리스트 초기화
fibo_cache = [0] * 100
def fibo_memoization(x):
    if x == 1 or x == 2:
        return 1

    # 이미 계산된 경우 저장된 값 반환
    if fibo_cache[x] != 0:
        return fibo_cache[x]

    # 캐쉬에 결과 기록
    fibo_cache[x] = fibo_memoization(x-1) + fibo_memoization(x-2)

    return fibo_cache[x]

# 반복문을 사용하여 상향식 알고리즘으로 변경한 버전
## 상향식 알고리즘에서 결과값을 저장하는 리스트를 DP(Dynamic Programming) table이라고 부른다.
def fibo_bottom_up():
    # 결과 값을 저장할 리스트 초기화
    dp_table = [0] * 100

    # 반복 문제에서 벗어나는 예외 단계는 직접 입력
    dp_table[1] = 1
    dp_table[2] = 1

    n = 99
    # 1, 2번 단계를 제외하고 99까지 실행
    for i in range(3, n+1):
        dp_table[i] = dp_table[i-1] + dp_table[i-2]

    return dp_table[n]
    

print(fibo_basic(4))
print(fibo_memoization(99))
print(fibo_bottom_up())