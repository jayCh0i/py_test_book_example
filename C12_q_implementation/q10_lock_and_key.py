# 열쇠를 자물쇠에 상하좌우 끝에서 한칸씩 걸치면서 확인해야 한다.
# 항상 자물쇠가 열쇠보다 같거나 크니까 자물쇠의 가로세로 3배되는 공간에다, 가운데에만 자물쇠를 두고
# 열쇠를 3배 공간의 0,0부터 한칸한칸 움직여가면서 처리해보자
# 모든 경우의 수를 돌려도 시간이 될까 싶지만, 1초는 꽤 기니까 그냥 차근차근 구현하면 된다

# 회전 방법은 공식이기 때문에 외워두면 편하다
def rotate_matrix(arr):
    row, col = len(arr), len(arr[0])

    # 회전됬을때 크기로 배열 초기화
    result = [[0] * row for _ in range(col)]

    for i in range(row):
        for j in range(col):
            result[j][(row - i) - 1] = arr[i][j]

    return result

# 정확히 결합되었는지 확인
def check_key_fit(expended_lock):
    # 확장 자물쇠 영역에서 진짜 자물쇠 배열의 크기를 구한다
    lock_size = len(expended_lock)//3
    
    # 진짜 자물쇠 부분만 확인한다
    for i in range(lock_size, lock_size*2):
        for j in range(lock_size, lock_size*2):
            if expended_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    key_size, lock_size = len(key), len(lock)

    # 자물쇠 9배 크기인 확장 자물쇠 영역을 생성
    expended_lock = [[0] * (lock_size*3) for _ in range(lock_size*3)]

    # 가운데에만 자물쇠 정보를 입력
    for i in range(lock_size):
        for j in range(lock_size):
            expended_lock[i+lock_size][j+lock_size] = lock[i][j]

    # 키를 총 네 번 회전시켜 맞춰본다
    for _ in range(4):
        # 열쇠 회전
        key = rotate_matrix(key)

        # 열쇠의 좌상단이 위치할 x,y 좌표, 범위는 더 줄일수있으나 간단하게 정한다
        ## 범위를 lock_size - key_size, lock_size*2 -1로 하면
        ## 키가 가운데 자물쇠 부분의 완전 밖에 있을때 연산은 생략시킬수 있긴 하다
        for x in range(lock_size*2):
            for y in range(lock_size*2):

                # 열쇠 좌상단을 현재 x,y 좌표에 두고 확장 자물쇠 영역에다 키를 넣는다
                for i in range(key_size):
                    for j in range(key_size):
                        expended_lock[x+i][y+j] += key[i][j]

                if check_key_fit(expended_lock) == True:
                    return True
                # 키를 빼서 열쇠 꼽기 전의 데이터로 돌린다
                for i in range(key_size):
                    for j in range(key_size):
                        expended_lock[x+i][y+j] -= key[i][j]

    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
val = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, val))