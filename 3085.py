# 3085 사탕 게임
n = int(input())
board = [list(input()) for _ in range(n)]

# 바꿨을 때 가장 길게 연결되는 것의 길이 반환
answer = 0


def check():
    global answer
    # 행 안에서 가장 긴 부분
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                cnt += 1
                if cnt > answer:
                    answer = cnt
            else:
                cnt = 1

    # 열 안에서 가장 긴 부분
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if board[j][i] == board[j+1][i]:
                cnt += 1
                if cnt > answer:
                    answer = cnt
            else:
                cnt = 1


# 인접한 두 개 교환하는 프로그램
# 열 안에서 교환
for i in range(n):
    for j in range(n-1):
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        check()
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

# 행 안에서 교환
for i in range(n):
    for j in range(n-1):
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
        check()
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(answer)
