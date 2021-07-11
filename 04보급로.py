import sys
sys.stdin = open('04.txt', 'r')


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    result = []
    Q = [(r, c)]
    D = [[9999] * N for _ in range(N)]
    D[r][c] = 0

    while Q:
        cur_r, cur_c = Q.pop(0)
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if D[cur_r][cur_c] + matrix[nr][nc] < D[nr][nc]:
                    Q.append((nr, nc))
                    D[nr][nc] = D[cur_r][cur_c] + matrix[nr][nc]
                    if (nr, nc) == (N - 1, N - 1):
                        result.append(D[nr][nc])
    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    print('#{} {}'.format(tc, min(bfs(0, 0))))