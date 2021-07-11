import sys

sys.stdin = open('1226.txt', 'r')


dr = [-1, 1, 0, 0] # 상하
dc = [0, 0, -1, 1] # 좌우


def bfs(r, c):
    global found
    Q = [(r, c)]

    while Q:
        cur_r, cur_c = Q.pop(0)
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == '3':
                    return 1
                if maze[nr][nc] != '1':
                    Q.append((nr, nc))
                    maze[nr][nc] = '1'
    return 0


def dfs(r, c):
    global found
    if maze[r][c] == '3':
        found = 1
        return

    maze[r][c] = '1'

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if maze[nr][nc] != '1':
                dfs(nr, nc)


T = 10
for _ in range(1, T + 1):
    tc = int(input())
    N = 16
    maze = [list(input()) for _ in range(N)]
    # visited = [[0 for _ in range(N)] for _ in range(N)]
    # 방문기록을 만들지 말고, 방문한다면 벽으로 만들자!

    s = (1, 1)
    found = 0

    # dfs(*s)
    print('#{} {}'.format(tc, bfs(*s)))