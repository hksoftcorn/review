# 자꾸 메모리 초과로 떠서,, 참고하여 작성했습니당
# reference : 박준규.py


# def decode(info):
#     codes = []
#     for i in range(8):
#         # code_number = ''.join(map(str, info[i * 7 : (i + 1) * 7]))
#         codes.append(int(numbers[code_number]))
#     return codes

def codes_sum(codes):    
    total = 0
    idx = 0    
    for code in codes:
        if idx % 2:
            total += int(code)
        else:
            total += (3 * int(code))
        idx += 1
    return total


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = []
    
    input_data = [list(input()) for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if input_data[r][c] == '1':
                end_r, end_c = r, c
    
    origin_codes = ''.join(input_data[end_r][end_c - 55 : end_c + 1])
    # print(origin_codes)
    my_dict = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }

    numbers = ''
    for i in range(8):
        code = origin_codes[i * 7: (i+1) * 7]
        numbers += str(my_dict[code])
    # print(numbers)

    total = codes_sum(numbers)
    print(total)
    ans = 0
    if total % 10 == 0:
        ans = sum([int(num) for num in numbers])
    print('#{} {}'.format(tc, ans))


    # # for info in input_data:
    # #     # result.append(info)
    # #     if info[-11] == 0: continue
    # #     # if info[-11]:
    # #     info = info[-66 : -10]
    # #     break



    # numbers = []
    # for i in range(8):
    #     origin_codes[]

    # codes = decode(origin_codes)
    # total = codes_sum(codes)
