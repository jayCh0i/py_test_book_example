# 원소 개수와 교환 횟수 입력 받음
n, m = map(int, input().split())

# 각각의 리스트 입력 받음
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# A는 오름차순, B는 내림차순 으로 정렬
a.sort()
b.sort(reverse=True)

# 교환 횟수만큼 교환 진행
for i in range(m):
    # B 원소이 A 원소값 보다 경우
    if a[i] < b[i]:
        # 교체 진행
        a[i], b[i] = b[i], a[i]
    else:
        # A 원소값이 이미 B 원소값보다 커진 경우 교환이 필요 없으므로 종료
        break

# 결과 출력
print(sum(a))