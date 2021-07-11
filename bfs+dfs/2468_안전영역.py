import sys
sys.setrecursionlimit(15000)

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
min_num = min([min(matrix[i]) for i in range(N)])
max_num = max([max(matrix[i]) for i in range(N)])


dr = [-1, 1, 0 , 0]
dc = [0, 0, -1, 1]
def dfs(r, c):
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # if 0 <= nr < N and 0 <= nc < N:
        if nr < 0 or N <= nr or nc < 0 or N <= nc: continue
        if not visited[nr][nc] and matrix[nr][nc] > num:
            dfs(nr, nc)


def bfs(r, c):
    Q = [(r, c)]
    visited[r][c] = 1

    while Q:
        cur_r, cur_c = Q.pop(0)
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if nr < 0 or N <= nr or nc < 0 or N <= nc: continue
            if not visited[nr][nc] and matrix[nr][nc] > num:
                visited[nr][nc] = 1
                Q.append((nr, nc))    


max_cnt = 1
for num in range(min_num, max_num):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and matrix[i][j] > num:
                cnt += 1
                bfs(i, j)
    max_cnt = max(cnt, max_cnt)

print(max_cnt)
