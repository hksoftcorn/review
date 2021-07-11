import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


for tc in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    to_visits = []

    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    cnt = 0
    for i in range(1, V + 1):
        if visited[i] == 0:
            cnt += 1
            to_visits.append(i)

        while to_visits:
            current = to_visits.pop()

            if not visited[current]:
                visited[current] = 1
                for v in G[current]:
                    if visited[v] == 0:
                        to_visits.append(v)

    print('#{} {}'.format(tc, cnt))