
move = [1, -1, 2]
def bfs(n):
    global cnt, dist
    visited = [0] * 100001
    
    Q = [n]
    visited[n] = 1
    while Q:
        cur_n = Q.pop(0)
        if cur_n == M:
            return
        for i in range(3):
            if i == 2:
                next_n = cur_n * move[2]
            else:
                next_n = cur_n + move[i]
            if 0 > next_n or next_n >= 100001: continue
            if not visited[next_n]:
                visited[next_n] = 1
                dist[next_n] = dist[cur_n] + 1
                Q.append(next_n)

N, M = map(int, input().split())
dist = [0] * 100001
bfs(N)
print(dist[M])