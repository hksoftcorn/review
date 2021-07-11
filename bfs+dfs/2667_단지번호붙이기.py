dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    Q = [(r, c)]
    arr[r][c] = 0
    ans = 1
    while Q:
        cur_r, cur_c = Q.pop(0)
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 1:
                    arr[nr][nc] = 0
                    ans += 1
                    Q.append((nr, nc))
    result.append(ans)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt += 1
            bfs(i, j)
result.sort()
result.insert(0, cnt)
for ele in result:
    print(ele)

