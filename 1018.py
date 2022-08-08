# 1018 체스판 다시 칠하기
n, m = map(int, input().split())

B_compare = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], [
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

W_compare = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], [
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

check = []
for i in range(n):
    check.append(list(input()))

answer = 65  # 다 다른 경우인 8*8보다 1 큰 수
for b in range(m-7):
    for a in range(n-7):
        B_cnt = 0
        W_cnt = 0

        for i in range(8):
            for j in range(8):
                if B_compare[i][j] != check[a+i][b+j]:
                    B_cnt += 1
                if W_compare[i][j] != check[a+i][b+j]:
                    W_cnt += 1

        temp = min(B_cnt, W_cnt)
        answer = min(answer, temp)

print(answer)
