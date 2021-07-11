import sys
sys.stdin = open('03.txt', 'r')



def find_asc(result, node):
    if node == 1:
        return

    idx = 1
    while not node in tree[idx]:
        idx += 1

    result.append(idx)
    find_asc(result, idx)


def count_subtree(node):
    global cnt
    if node:
        cnt += 1
        count_subtree(tree[node][0])
        count_subtree(tree[node][1])


T = int(input())
for tc in range(1, T + 1):
    V, E, node_1, node_2 = map(int, input().split())
    tree = [[0] * 2 for _ in range(V + 1)]
    info = list(map(int, input().split()))

    for i in range(E):
        parent, child = info[i * 2 : (i + 1) * 2]
        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child

    result_1 = []
    result_2 = []
    find_asc(result_1, node_1)
    find_asc(result_2, node_2)

    same_asc = 0
    if len(result_1) >= len(result_2):
        for ele in result_1:
            if ele in result_2:
                same_asc = ele
                break
    else:
        for ele in result_2:
            if ele in result_1:
                same_asc = ele
                break
    cnt = 0
    count_subtree(same_asc)
    print('#{} {} {}'.format(tc, same_asc, cnt))


# 문제를 잘못읽어서 접근이 이상했다..
# 부모노드가 자식노드보다 크다는 전제를 깔고 문제를 풀었지만,,, -> 문제에 명시되어있다..
# def solution(result, node, target_node):
#     if tree[node][0]:
#         solution(result, tree[node][0], target_node)
#         solution(result, tree[node][1], target_node)
#
#     if node == target_node:
#         result.append(i)
#
#
# def subtree(node):
#     global cnt
#     if tree[node][0]:
#         cnt += 1
#         subtree(tree[node][0])
#         subtree(tree[node][1])
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     V, E, node_1, node_2 = map(int, input().split())
#     tree = [[0] * 2 for _ in range(V + 1)]
#     info = list(map(int, input().split()))
#
#     for i in range(E):
#         parent, child = info[i * 2 : (i + 1) * 2]
#         if tree[parent][0] == 0:
#             tree[parent][0] = child
#         else:
#             tree[parent][1] = child
#
#     result1 = []
#     for i in range(node_1):
#         solution(result1, i, node_1)
#
#     result2 = []
#     for i in range(node_2):
#         solution(result2, i, node_2)
#
#     # result1 뒤에서부터 숫자를 가져옵니다
#     # result2 리스트에 원소가 있는 지 확인합니다.
#     ans = 0
#     for ele in result1[::-1]:
#         if ele in result2:
#             ans = ele
#             break
#
#     print(result1, result2, ele)
#     # cnt = 0
#     # subtree(ans)
#     # print(ans, cnt)


