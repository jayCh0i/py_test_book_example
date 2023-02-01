n = int(input())
k = int(input())

board = [[0] * n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1

o = int(input())

ops = []
for _ in range(o):
    a, b = input().split()
ops.append((int(a), b))

head_loc = [0, 0]

direction = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

length = 1
body = []
count = 0

def forward():
    return 1


def turn(o):
    if o == 'L':
        direction + 2
    else:
        direction - 2
    return 1

while 0 <= head_x < n and 0 <= head_y < n and board[head_y][head_x] > 0:



