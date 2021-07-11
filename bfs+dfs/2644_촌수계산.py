V = int(input())
n1, n2 = map(int, input().split())
E = int(input())

tree = [[] for _ in range(V + 1)]
for _ in range(E):
    p, c = map(int, input().split())
    tree[p].append(c)
"""i.g.
0 : [],
1 : [2, 3],
2 : [7, 8, 9],
3 : [],
4 : [5, 6],
5 : [],
6 : [],
7 : []
"""

# 공통 조상 찾기
def asc(result, node):
    idx = 1
    while not node in tree[idx]:
        if idx == V:
            return
        idx += 1
    result.append(idx)
    asc(result, idx)

result1 = [n1]
result2 = [n2]
asc(result1, n1)
asc(result2, n2)
# print(result1, result2)

same_asc = []
if len(result1) >= len(result2):
    for r1 in result1:
        if r1 in result2:
            same_asc += [r1]
            break
else:
    for r2 in result2:
        if r2 in result1:
            same_asc += [r2]
            break
# print(same_asc[0])

# def find_subtree(cnt, asc_node, target_node):
#     if asc_node == target_node:
#         return cnt
#     else:
#         if tree[asc_node]:
#             cnt += 1
#             find_subtree(cnt, tree[asc_node].pop(), target_node)

def subtree(node):
    Q = [node]
    visited = [0] * (V + 1)
    visited[node] = 1
    distance = [0] * (V + 1)

    while Q:
        current = Q.pop(0)
        # if current == n1:
        #     return distance[n1]
        for w in tree[current]:
            if not visited[w]:
                Q.append(w)
                # cnt += 1
                distance[w] = distance[current] + 1
                visited[w] = 1
    return distance


if not len(same_asc):
    print(-1)
else:
    distance = subtree(same_asc[0])
    print(distance[n1] + distance[n2])