"""
출발지점 A : 0 
도착지점 B : 99 
한 개의 정점에서 선택할 수 있는 정점의 수는 최대 2개
A 에서 출발하여 B에 도착한다면 True: 1 / False: 0
dfs를 이용합니다.
"""
import sys
sys.stdin = open('01.txt', 'r')

def dfs(v):
    visited[v] = 1

    for w in G[v]:
        if not visited[w]:
            dfs(w)

T = 10
for _ in range(T):
    tc, E = map(int, input().split())
    G = [[] for _ in range(100)]
    visited = [0] * 100
    """
    G = [
      1:  [],
      2:  []
    ]
    """
    input_data = list(map(int, input().split()))

    # 1. G 그래프를 그립니다.
    for i in range(E):
        u, v = input_data[i * 2: (i + 1) * 2]
        G[u].append(v)

    # 2. dfs 구현
    dfs(0)
    print(f'#{tc} {visited[99]}')