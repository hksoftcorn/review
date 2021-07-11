import sys
sys.stdin = open('02.txt', 'r')


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    global found
    Q = [(r, c)]
    matrix[r][c] = '1'

    while Q:
        cur_r, cur_c = Q.pop(0)
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if matrix[nr][nc] == '3':
                    return 1
                if matrix[nr][nc] != '1':
                    Q.append((nr, nc))
                    matrix[nr][nc] = '1'
    return 0


T = 10
for _ in range(T):
    tc = int(input())
    N = 100
    matrix = [list(input()) for _ in range(N)]

    s = (1, 1)
    found = 0

    print(f'#{tc} {bfs(*s)}')