# Spanning Tree

## concept

`신장트리(Spanning Tree)`란 (1) 원 그래프의 모든 노드를 포함하고 (2) 모든 노드가 서로 연결되어 있으면서 (3) 트리(Tree)의 속성을 만족하는 그래프를 가리킵니다. 최소신장트리(MST)는 가능한 신장트리 가운데 엣지 가중치의 합이 최소인 신장트리를 말합니다. 

MST는 노드 간 연결성을 보장하면서 노드 사이를 잇는 거리/비용 등을 최소로 하는 그래프를 의미하기 때문에 응용 범위가 넓습니다. 이 글에서는 원 그래프에서 MST를 찾아내는 기법인 **크루스칼 알고리즘(Kruskal’s algorithm)**과 **프림 알고리즘(Prim’s algorithm)**을 살펴보도록 하겠습니다.

> Why we learn **MST** ? 
>
> i.g. 시골에 다섯 집이 있다고 하자. 모든 집집마다 전기를 공급하고자 하는데, 연결하는 전기선이 최소가 되는 방법을 찾는다면? MST를 이용하면 찾기 쉽다!

## 1. MST

### 1.1. 크루스칼 알고리즘(Kruskal’s algorithm)

```python
for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    edges = [list(map(int, input().split())) for _ in range(E)]

    #------------------------------------
    # disjoint-set
    p = [i for i in range(V + 1)]
    def findSet(v):
        if v != p[v]:
            p[v] = findSet(p[v])
        return p[v]
    #------------------------------------

    edges.sort(key=lambda e: e[2], reverse=True)
    cnt = ans = 0
    while cnt < V:  # 정점수 = V + 1, 간선수 = V
        u, v, w = edges.pop()
        a, b = findSet(u), findSet(v)
        if a == b: continue
        p[b] = a
        ans += w
        cnt += 1

    print('#{} {}'.format(tc, ans))
```



### 1.2. 프림 알고리즘(Prim’s algorithm)

```python
for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))

    MST = [False] * (V + 1)
    key = [0xffffff] * (V + 1)
    key[0] = 0
    ans = 0

    for _ in range(V + 1):
        # key 값이 최소인 정점 찾기
        u, min_key = 0, 0xfffffff
        for i in range(V + 1):
            if not MST[i] and min_key > key[i]:
                u, min_key = i, key[i]

        # 트리에 포함된 정점으로 표시
        MST[u] = True
        ans += key[u]

        for v, w in G[u]:
            if not MST[v] and key[v] > w:
                key[v] = w

    print('#{} {}'.format(tc, ans))
```

