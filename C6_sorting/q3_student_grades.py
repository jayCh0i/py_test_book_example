# 학생 수 입력 받음
n = int(input())

# 학생 정보 리스트 초기화
array = []

# 튜플에서 점수 값을 반환하는 함수
def return_student(data):
    return data[1]

# 학생 수 만큼 입력 받음
for i in range(n):
    input_data = input().split()

    ## (이름, 점수) 형태의 튜플로 리스트에 추가한다
    array.append((input_data[0], int(input_data[1])))

# 점수 값을 기준으로 정렬하도록 key값을 정한다
## key 파라미터에 간결한 람다식을 활용하여 튜플에서 점수 값을 반환하도록 한다.
array.sort(key= lambda student: student[1])

## 람다식을 사용하지 않고 함수를 넘겨주는 방식으로 하였을때
# array.sort(key=return_student)

# 결과 출력
for i in array:
    print(i[0], end='')