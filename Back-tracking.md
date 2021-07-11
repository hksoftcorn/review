[TOC]

# 완전검색 & Back-tracking 복습

### 완전검색

모든 경우의 수를 고려합니다. 트리를 그려보면서 패턴을 찾고 재귀로 풀어낼 수 있습니다. 백트래킹과 동적계획법은 완전 검색을 조금 더 스마트하게 해결하는 방법을 말합니다.

- Back-tracking
- DP 동적 계획법

#### 1. 순열

```python
# 1. for문
arr = ['A', 'B', 'C', 'D']
N = len(arr)

for i in range(0, N):
    arr[0], arr[i] = arr[i], arr[0]
    
    for j in range(1, N):
        arr[1], arr[i] = arr[i], arr[1]

        for k in range(2, N):
        	arr[2], arr[k] = arr[k], arr[2]
		    print(arr) # 바꾼 상태를 출력하고
	        arr[2], arr[k] = arr[k], arr[2]
            
        arr[1], arr[i] = arr[i], arr[1]
	    
    arr[0], arr[i] = arr[i], arr[0] # 원상 복귀!

    
# 2. 재귀호출
def perm(k):		# k: 함수 호출의 높이
    if k == N:
        print(arr)
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k + 1)
            arr[k], arr[i] = arr[i], arr[k]

perm(0)
```

- 초기상태에서 상태공간 트리를 만들게 됩니다.
- 첫 번째 자리에 들어갈 수 있는 인자로 'A', 'B', 'C', 'D' 4가지가 있습니다.
  - idx요소로 자리를 교환한다고 표현하면 (0, 0) (0, 1) (0, 2) (0, 3) 이 됩니다.
  - 자리를 바꾼 값들이 그대로 저장되어 원복형태를 해치게 됩니다.
- A 다음에 두 번째 자리에 들어갈 수 있는 인자로 'B', 'C', 'D' 3가지가 있습니다.
  - (1, 1) (1, 2) (1, 3)

##### 최적 경로

- 문제 설명 : 출발지에서 출발하여 가장 짧은 경로로 모든 노드를 거치고 도착지에 도착하는 경로를 찾아라
- 이론 : 최적화 문제 + 완전 그래프
  - 조건을 만족하는 해(후보 해) 중에서 가장 최소가 되는 값을 찾으면 됩니다.
  - 최적화 문제는 우선적으로 `완전 검색`을 해야 합니다.
  - *TSP* (*Traveling Salesman Problem*) 이란 문자 그대로, 물건을 판매하기 위해 여행하는 세일즈맨의 문제입니다.
  - Force가 많이 필요합니다 → CPU 사용률이 높습니다. 
    - P : 쉬운 문제, big O 표현식이 다항식에 들어오는 문제라면 (컴퓨터에게) 쉬운 문제라고 분류합니다.
    - ~P : 어려운 문제, 지수 혹은 팩토리얼 계산식이 들어가면서 수많은 연산을 요구합니다.
- 컨셉 : 

```python
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


```



#### 2. 부분집합

```python
# bit 표현식
# 원소의 개수만큼 for문을 중첩합니다.
for i in range(2): # 0, 1
    for j in range(2): # 0, 1
        for k in range(2): # 0, 1
            print(i, j, k)

           
arr = 'ABC'; N = len(arr)
bits = [0] * N
for i in range(2): # 0, 1
    bits[0] = i
    for j in range(2): # 0, 1
        bits[1] = j
        for k in range(2): # 0, 1
            bits[2] = k
            print(i, j, k, end=' --> ')
            for l in range(N):
                if bits[l]: print(arr[l], end=' ')
            print()
            
# 재귀 표현식
arr = 'ABC'; N = len(arr)
bits = [0] * N
def backtrack(k): # k: 함수호출 트리에서의 높이, 지금까지 선택한 개수
    if k == N:
        for l in range(N):
            if bits[l]: print(arr[l], end=' ')
        print()
    else:
        # N개가 만족하지 않는다면
        # for i in range(2):
        #    bits[k] = i
        #    backtrack(k + 1)
        bits[k] = 0  
        backtrack(k + 1) 
        bits[k] = 1
        backtrack(k + 1)    
        
backtrack(0)  # 0번째 부터 비트를 표현합니다
```

```python
arr = [3, 5, 1, 6]; N = len(arr)
bits = [0] * N

def backtrack(k, cur_sum):	# k: 함수호출 트리에서의 높이, 지금까지 선택한 개수
    if k == N:				# cur_sum: 지금까지 포함히기로 선택한 원소들 합
        s = 0
        for i in range(N):
            if bits[i]:
                s += arr[i]
        print(s)
    else:
        bits[k] = 1			# k번 원소를 부분집합에 포함하는 선택
        backtrack( k + 1, cur_sum + arr[k] )
        bits[k] = 0			# k번 원소를 부분집합에 포함하지 않는 선택
        backtrack( k + 1, cur_sum )
```

```python
arr = [3, 5, 1, 6]; N = len(arr)
bits = [0] * N
M = 6

def backtrack(k, cur_sum):	# k: 함수호출 트리에서의 높이, 지금까지 선택한 개수
    if cur_sum > M:			# cur_sum: 지금까지 포함히기로 선택한 원소들 합
        return 
    if k == N:				
		if cur_sum == M:
	        for i in range(N):
	            if bits[i]:
	                print(arr[i], end=' ')
            print()
    
    else:
        bits[k] = 1			# k번 원소를 부분집합에 포함하는 선택
        backtrack( k + 1, cur_sum + arr[k] )
        bits[k] = 0			# k번 원소를 부분집합에 포함하지 않는 선택
        backtrack( k + 1, cur_sum )
        
backtrack(0, 0)
```

```python
arr = [3, 5, 1, 6]; N = len(arr)
bits = [0] * N
M = 6

def backtrack(k, cur_sum):	# k: 함수호출 트리에서의 높이, 지금까지 선택한 개수
    if cur_sum > M:			# cur_sum: 지금까지 포함히기로 선택한 원소들 합
        return 
    if k == N:				
		if cur_sum == M:
            # 답을 저장
    
    else:
        backtrack( k + 1, cur_sum + arr[k] )
        backtrack( k + 1, cur_sum )

backtrack(0, 0)
```

##### 장훈이의 높은 선반

```python
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
```

