# Tree 복습

##### 기본 이진트리 

```python
import sys; sys.stdin = open('input.txt', 'r')
# 13 12
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

V, E = map(int, input().split())
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)
arr = list(map(int, input().split()))

for i in range(0, E * 2, 2):
    p, c = arr[i], arr[i + 1]
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    P[c] = p

def inorder(v):
	if v == 0: return 
    # 전위
    inorder(L[v])
    # 중위
    print(v, end=' ')
    inorder(R[v])
    # 후위

inorder(1)
```

1. 트리의 높이를 계산해서 출력하시오.  treeHeight(3) --> 3
2. 높이가 3인 노드들을 출력하시오. (7, 8, 9, 10, 11)
3. 3번 노드가 루트인 트리의 전체 노드수 treeSize(3) --> 8
4. 8번 노드와 10번 노드의 공통조상을 출력하시오. (1, 3)



##### 공통조상 (=Lowest Common Ancestor)

```python
# LCA 찾기

# v = n1
# v = p[v]
def findLCA():
    tmp = []	# set() 쓰는게 좋다
    v = P[n1]
    while v:
        tmp.append(v)
        v = P[v]
        
    v = P[n2]
    while v:
        if v in tmp:	# list에서 순차검색을 하기 때문에 set쓰자
            break
    return v

def treeSize(v):
    global cnt
    if v == 0: return
    cnt += 1
    treeSize(L[v])
    treeSize(R[v])

for tc in range(1, int(input()) + 1):
    V, E, n1, n2 = map(int, input().split())
    arr = list(map(int, input().split()))
    L = [0] * (V + 1)
    R = [0] * (V + 1)
    P = [0] * (V + 1)
    for i in range(0, len(arr), 2):
        p, c = arr[i], arr[i + 1]
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
        P[c] = p
        
    cnt = 0
    lca = findLCA()
    treeSize(lca)
    print('#{} {}'.format(tc, cnt))
```

