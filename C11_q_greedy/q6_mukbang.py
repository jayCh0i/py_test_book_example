import heapq

# 시간이 지날수록 비우는 음식이 늘어나고 이는 음식판에 음식 개수가 바뀌어 단순 반복 계산하는데에 문제가 있다.
# 이를 제일 적은 음식을 다 먹을때 까지 모든 음식을 돌아가면서 먹는 것을 단계로 구분하여 시간을 계산해 나가는 식으로 해결해보자
def solution(food_times, k):
    # 남은 음식의 양이 주어진 시간보다 적은경우 종료
    if sum(food_times) < k :
        return -1

    # 힙 변수 초기화. 최소힙을 이용해 제일 적은양의 음식을 구하기 위함
    q = []

    # 힙큐에 (음식의 양 , 음식 번호)로 저장
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    # 지금까지 음식을 먹은 시간
    total_time = 0
    # 최근에 비운 음식의 양, 최소힙에서 작은것부터 가져오므로 점차 증가한다
    prev_food = 0
    # 남은 음식 개수
    food_cnt = len(food_times)
    
    # 한 음식이 비워질때까지 모든 음식을 돌아가면서 먹어도 시간이 남을때까지 반복한다
    while total_time + ((q[0][0]  - prev_food) * food_cnt) <= k:
        # 남은 음식 중 제일 적은 음식양을 가져온다
        now = heapq.heappop(q)[0]
        # 지금 음식을 비울때 까지 걸리는 시간을 구한다. 지금 음식의 남은 양은 이전의 음식을 비우면서 그 양만큼 감소했으니 이를 감안해서 계산한다
        total_time += (now - prev_food) * food_cnt
        # 남은 음식 개수는 줄어든다
        food_cnt -= 1
        # 지금 비운 음식의 양을 기록한다
        prev_food = now

    # 이제 남은 시간보다 한 음식을 비울때까지 걸리는 시간이 큰 경우다
    # 남은 음식들을 번호대로 정렬하고, 남은 시간을 가지고 계산한다
    leftovers = sorted(q, key= lambda x: x[1])



k = int(input())

food_times = list(map(int, input().split()))

print(solution(food_times, k))