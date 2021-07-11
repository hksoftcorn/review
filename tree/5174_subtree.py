def solution(node):
    global cnt
    cnt += 1
    children = tree[node]
    for child in children:
        solution(child)


T = int(input())
for tc in range(1, T+1):
    E, V = map(int, input().split())
    input_data = list(map(int, input().split()))
    tree = [[] for _ in range(E + 2)]
    for i in range(E):
        p, c = input_data[i * 2: (i + 1) * 2]
        tree[p].append(c)
    cnt = 0
    solution(V)
    print('#{} {}'.format(tc, cnt))


    