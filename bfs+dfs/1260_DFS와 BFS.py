def dfs(v):
    visited[v] = 1
    
    for w in sorted(G[v]):
        if not visited[w]:
            dfs_path.append(w)
            dfs(w)

def bfs(v):
    visit = [0] * (N+1)
    visit[v] = 1
    Q = [v]

    while Q:
        current = Q.pop(0)
        for w in sorted(G[current]):
            if not visit[w]:
                visit[w] = 1
                bfs_path.append(w)
                Q.append(w)

N, E, V = map(int, input().split())
G = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

dfs_path = [V]
dfs(V)
print(' '.join(map(str, dfs_path)))
bfs_path = [V]
bfs(V)
print(' '.join(map(str, bfs_path)))