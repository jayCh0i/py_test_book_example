# 문자열 입력 받음
str = input()

# 0으로 뒤집는 경우 횟수와 1로 뒤집는 휫수 변수 초기화
flip_to_zero = 0
flip_to_one = 0

# 첫 원소에 대해 처리 뒤집기 횟수 추가
if str[0] == '1':
    flip_to_zero += 1
else:
    flip_to_one += 1

# 다음 원소와 비교 해나가면서 문자열 전체를 확인
for i in range(len(str)-1):
    # 다음 값이 지금과 다르면 뒤집기 횟수 추가
    if str[i] != str[i+1]:
        if str[i+1] == '1':
            flip_to_zero += 1
        else:
            flip_to_one += 1

# 둘중에 적은 결과 출력
print(min(flip_to_zero, flip_to_one))

