import sys; sys.stdin = open('05.txt', 'r')


def dist(arr):
    cnt = 0
    for i in range(N + 1, 0, -1):
        x = abs(arr[i][0] - arr[i-1][0])
        y = abs(arr[i][1] - arr[i-1][1])
        cnt += x + y
    return cnt

def perm(k):
    global min_dist
    if k == N + 1:
        tmp = dist(pos)
        if min_dist > tmp:
            min_dist = tmp

    else:
        for i in range(k, N + 1):
            pos[k], pos[i] = pos[i], pos[k]
            perm(k + 1)
            pos[k], pos[i] = pos[i], pos[k]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    G = [0] * (N + 2)
    visited = [0] * (N + 2)
    arr = list(map(int, input().split()))

    pos = [[arr[0], arr[1]]]
    for i in range(4, (N + 2) * 2, 2):
        pos.append([arr[i], arr[i + 1]])
    pos.append([arr[2], arr[3]])
    min_dist = 0xffffff

    perm(1)
    print('#{} {}'.format(tc, min_dist))