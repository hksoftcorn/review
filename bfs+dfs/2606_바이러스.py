def dfs(v):
    global cnt
    visited[v] = 1
    for w in G[v]:
        if not visited[w]:
            cnt += 1
            dfs(w)

N = int(input())
E = int(input())
G = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

# 그래프를 그려줍니다.
for i in range(E):
    v, u = map(int, input().split())
    G[v].append(u)
    G[u].append(v)

cnt = 0
dfs(1)
print(cnt)