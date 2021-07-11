T = int(input())
for tc in range(1, T+1):
    V, M, L = map(int, input().split())
    tree = [[0, 0, 0] for _ in range(V + 1)]
    for node in range(1, V+1):
        if node * 2 <= V:
            tree[node][0] = 2 * node
            if node * 2 + 1 <= V:
                tree[node][1] = 2 * node + 1
    
    for node in range(M):
        p, number = map(int, input().split())
        tree[p][2] = number
    
    for node in range(V - M, 0, -1):
        tree[node][2] = tree[node * 2][2]
        if node * 2 + 1 <= V:
            tree[node][2] += tree[node * 2 + 1][2]
        if node == L:
            print(f'#{tc} {tree[node][2]}')