def backtrack(k, cur_sum):
    global result
    if k == N:
        if cur_sum >= M:
            result.add(cur_sum)
    else:
        backtrack(k + 1, cur_sum + arr[k])
        backtrack(k + 1, cur_sum)


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    result = set()
    
    backtrack(0, 0)
    print('#{} {}'.format(tc, min(result) - M))
