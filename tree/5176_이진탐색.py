"""
포화이진트리 형태에서 사용할 수 있습니다.

"""
def solution(v):
    global cnt
    if v > 0:
        solution(tree[v][0])
        cnt += 1
        tree[v][2] = cnt
        solution(tree[v][1])


T = int(input())

for tc in range(1, T+1):
    V = int(input())
    tree = [[0] * 3 for _ in range(V + 1)]

    for node in range(1, V+1):
        if node * 2 <= V:
            tree[node][0] = 2 * node # 왼쪽 노드
            if node * 2 + 1 <= V:
                tree[node][1] = 2 * node + 1
    cnt = 0
    solution(1)
    
    print(f'#{tc} {tree[1][2]} {tree[V//2][2]}')
