# APS 복습

## 1. Intro

10억 개의 숫자를 정렬하는데 PC에서 O(n^2) 알고리즘은 300여 년이 걸리는 반면에 O(nlogn) 알고리즘은 5분 만에 정렬한다. 즉 효율적인 알고리즘은 슈퍼컴퓨터보다 더 큰 가치가 있으며 값 비싼 H/W의 기술 개발보다 효율적인 알고리즘 개발이 훨씬 더 경제적이다.



## 2. 완전 검색 & 그리디





## 3. 분할 정복 & 백트래킹



### 3.2. 백트래킹

##### Overview

백트래킹은 선택한 길을 되돌리는 것. 즉 갈림길이 있을 때, 선택을 해서 어떠한 길을 나아갈 때 앞에 미래가 없다면 빨리 포기해서, 다시 갈림길로 돌아와서 안 가본 길을 가보는 것이 백트래킹이 됩니다. 내가 선택(조사)해야 하는 모든 과정을 상태 공간 트리에 그리게 됩니다. 

SWEA [프로세서](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4suNtaXFEDFAUf&categoryId=AV4suNtaXFEDFAUf&categoryType=CODE&problemTitle=%ED%94%84%EB%A1%9C%EC%84%B8%EC%84%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&) 문제를 예로 들어봅시다. 최대한 많은 Core에 전원을 연결하되 전선 길이의 합은 최소가 되는 방법을 구해야 합니다. n개의 코어를 선택하는 상태 공간 그래프 그리게 됩니다. 연결하거나 연결하지 않는 선택을 합니다. 연결을 하게 되면 상/하/좌/우 연결 방법을 선택하게 됩니다. 5개의 상태 공간이 작은 서브셋 트리가 됩니다. 선택을 하면서 불가능한 상황에 처하면 이전 상태로 돌아가는 백트래킹 작업을 수행해야 합니다.

##### What

##### How

##### Why



## 4. 그래프

> - SWEA [7465 창용 마을 무리의 개수](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWngfZVa9XwDFAQU&categoryId=AWngfZVa9XwDFAQU&categoryType=CODE&problemTitle=%EC%B0%BD%EC%9A%A9+%EB%A7%88%EC%9D%84&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)
> - 백준 [2667 단지번호붙이기](https://www.acmicpc.net/problem/2667)

ⓐ경로 유무, ⓑ연결 컴포넌트(Connected Component) 세트

연결 컴포넌트를 연습할 수 있는 쉬운 문제하나 : SWEA [7465 창용 마을 무리의 개수](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWngfZVa9XwDFAQU&categoryId=AWngfZVa9XwDFAQU&categoryType=CODE&problemTitle=%EC%B0%BD%EC%9A%A9+%EB%A7%88%EC%9D%84&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1) 문제를 풀어봅시다. 사람은 1번부터 N번 사람까지 번호가 붙어져 있다고 가정한다. 두 사람은 서로를 알고 있는 관계일 수 있고, 아닐 수 있다. 두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면, 이러한 사람들을 모두 다 묶어서 하나의 무리라고 한다. 창용 마을에 몇 개의 무리가 존재하는지 계산하는 프로그램을 작성하라. 방문하지 않은 정점 하나를 선택하여 DFS를 이용하고 더 이상 갈 노드가 없다면, 다시 방문하지 않은 정점 하나를 선택하여 DFS를 이용합니다.백준 [2667 단지번호붙이기](https://www.acmicpc.net/problem/2667) 문제로 응용해봅시다.

BFS는 목표지점까지 최단거리로 찾아가게 됩니다. DFS는 목표 지점에 여러 번 방문하게 되지만, BFS는 최초 목표 지점에 방문하는 시점이 최단거리가 됩니다.

##### 7465_ 창용 마을 무리의 개수

```python
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
```

##### 2667_단지번호붙이기

```python
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    Q = [(r, c)]
    arr[r][c] = 0
    ans = 1
    while Q:
        cur_r, cur_c = Q.pop(0)
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 1:
                    arr[nr][nc] = 0
                    ans += 1
                    Q.append((nr, nc))
    result.append(ans)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt += 1
            bfs(i, j)
result.sort()
result.insert(0, cnt)
for ele in result:
    print(ele)
```

### 4.1. DFS

DFS 푸는 방법은 방법문과 재귀 방법이 있습니다. DFS는 재귀 방법으로 풉시다. (재귀가 아닌 방법으로도 구현이 가능해야 문제에서 응용이 가능합니다 :D )

그래프를 컴퓨터가 이해할 수 있도록 표현할 수 있는 것은 정점이 필요하며 정점사이에는 간선이 존재하게 됩니다.  여기서 간선을 표현한다는 것은 개체들 사이의 관계를 맺어준다는 것입니다. 예로 사람들이 정점이 되고 친구라는 관계는 간선이 된다는 것입니다. 다시 돌아와 정점은 N개가 주어지고, 

특정 정점의 인접 정점이 무엇이 있는 지 확인합니다.

```python
"""
7 8  # V, E
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
"""
V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
visit = [0] * (V + 1)

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1, V + 1):
    print(i, '-->', G[i])
    
def dfs(v): # v: 방문하는 정점 번호
    visit[v] = 1 # 방문한다
    print(v, end=' ')
    # 방문하지 않은 인접 정점을 찾는다.
    # v의 인접 정점은 G[v]
    for w in G[v]:
        if visit[w] == 0:
            dfs(w)
            
dfs(1)    
```

##### 길찾기

```python
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
```

##### 미로1

```python
import sys
sys.stdin = open('1226.txt', 'r')


dr = [-1, 1, 0, 0] # 상하
dc = [0, 0, -1, 1] # 좌우


def bfs(r, c):
    global found
    Q = [(r, c)]

    while Q:
        cur_r, cur_c = Q.pop(0)
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == '3':
                    return 1
                if maze[nr][nc] != '1':
                    Q.append((nr, nc))
                    maze[nr][nc] = '1'
    return 0


def dfs(r, c):
    global found
    if maze[r][c] == '3':
        found = 1
        return

    maze[r][c] = '1'

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if maze[nr][nc] != '1':
                dfs(nr, nc)

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    N = 16
    maze = [list(input()) for _ in range(N)]
    # visited = [[0 for _ in range(N)] for _ in range(N)]
    # 방문기록을 만들지 말고, 방문한다면 벽으로 만들자!

    s = (1, 1)
    found = 0

    # dfs(*s)
    print('#{} {}'.format(tc, bfs(*s)))
```



### 4.2. BFS

BFS는 반복문 방법으로 풉시다. BFS는 목표지점까지 최단경로를 찾을 때 사용됩니다.

너비우선탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식입니다. 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야하므로, 선입선출 형태의 자료구조인 큐를 활용합니다.

시작점에서 거리가 1인 정점들을 찾고 → 1인 정점을 이용하여 거리가 2인 정점들을 찾고 → ... 원하는 Target 정점을 찾을 수 있습니다. DFS와 달리 최단으로 목표지점에 방문을 한다는 것입니다.

```python
def BFS(G, v):
    visited = [0] * n
    queue = []
    queue.append(v)
    while queue:
        current = queue.pop(0)
        #visited[current] = 1  # 메모리 중복이 발생하므로 인접정점을 넣기 직전에 방문표시!
        for w in G[current]:
            if not visited[w]:
                visited[current] = 1
                queue.append(w)            
```

##### 추가 개념

두 가지 추가적인 정보를 계산해봅니다. `D`는 시작점에서 각 정점까지의 최단거리를, `P`는 최단경로트리를 저장하게 됩니다. 단, queue에서 꺼내온 정점을 v라고 하고, v의 인접 정점을 w라고 합니다. 

- D[w] = D[v] + 1
- P[w] = v

가중치가 주어진다면? D[w] = D[v] + (가중치) 로 표현할 수 있습니다. 이때 visited의 의미는 퇴색되게 됩니다. (∵ 짧은 거리를 가더라도 가중치 값들의 합이 크다면, 옳바른 결과를 나타낼 수 없습니다.) 또한 만약 D[w]가 작다면 새롭게 덮어 쓸 수 있도록 D의 초기값을 매우 큰 값으로 설정해둡니다. 

- `간선완화 (Edge Relaxation)` = if D[v] < D[w] 이라면 새로운 값으로 갱신하게 됩니다.

```python
V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
visit = [0] * (V + 1)

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)


def BFS(s):		# 시작 점
    queue = [s]
    visit[s] = 1
    
    while queue:
        v = queue.pop(0)
        for w in G[v]:
            if not visited[w]:
                visited[w] = 1
                queue.append(w)            
```

```python
V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]  # 인접 리스트
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

def bfs(s):     # 시작점
    visit = [0] * (V + 1)  # 방문 정보
    D = [0] * (V + 1)
    P = [0] * (V + 1)
    Q = [s]
    visit[s] = 1

    while Q:                # 빈 큐가 아닐 동안
        v = Q.pop(0)
        for w in G[v]:      # v --> w(인접정점)
            if visit[w] == 0:
                visit[w] = 1
                D[w] = D[v] + 1
                P[w] = v
                Q.append(w)
    print(D[1:])
    print(P[1:])
bfs(1)
```

##### 미로2

```python
import sys
sys.stdin = open('02.txt', 'r')


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    global found
    Q = [(r, c)]
    matrix[r][c] = '1'

    while Q:
        cur_r, cur_c = Q.pop(0)
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if matrix[nr][nc] == '3':
                    return 1
                if matrix[nr][nc] != '1':
                    Q.append((nr, nc))
                    matrix[nr][nc] = '1'
    return 0


T = 10
for _ in range(T):
    tc = int(input())
    N = 100
    matrix = [list(input()) for _ in range(N)]

    s = (1, 1)
    found = 0

    print(f'#{tc} {bfs(*s)}')
```

##### 보급로

```python
from collections import deque

diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for tc in range(1, int(input()) + 1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]
    D = [[0x1000000] * N for _ in range(N)]
    
    Q = deque()
    Q.append((0, 0))
    D[0][0] = MAP[0][0]

    while Q:
        x, y = Q.popleft()

        for dx, dy in diff:
            tx, ty = x + dx, y + dy
            if tx < 0 or tx == N or ty < 0 or ty == N: continue
            if D[tx][ty] > D[x][y] + MAP[tx][ty]:
                D[tx][ty] = D[x][y] + MAP[tx][ty]
                Q.append((tx, ty))

    print('#{} {}'.format(tc, D[N - 1][N - 1]))
```



## 5. 문자열





## 6. DP-1





## 7. DP-2





## 8. Math & Probability





