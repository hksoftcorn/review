"""
0 : 이동불가
1 : 통로
(1, 1) : 시작점
(N, M) : 도착점
"""
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
s = (0, 0)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 0

def bfs(s):
    global cnt
    Q = [s]
    D = [[0xfffffff] * M for _ in range(N)]
    D[s[0]][s[1]] = 1

    while Q:
        r, c = Q.pop(0)

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # if 0 <= nr < N and 0 <= nc < M:
            if 0 > nr or N <= nr or 0 > nc or M <= nc: continue
            if D[nr][nc] > D[r][c] + maze[r][c]:
                D[nr][nc] = D[r][c] + maze[r][c]
                if maze[nr][nc] == 1:
                    Q.append((nr, nc))

    return D[N-1][M-1]

print(bfs(s))
