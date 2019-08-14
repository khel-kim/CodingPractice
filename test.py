# T = int(input())
# data = []
# for _ in range(T):
#     str1 = input()
#     str2 = input()
#     data.append([str1, str2])
#
#
# def search(str1, window):
#     start = len(str1)
#     index = list(range(len(str1) - 1, -1, -1))
#     # print(str1, window)
#     for i in index:
#         if str1[i] == window[i]:
#             result = 1
#         else:
#             result = 0
#             current = window[i]
#             # print(current, 'current')
#             for j in index:
#                 if str1[j] == current:
#                     start = i - j
#                     break
#             break
#     return start, result
#
#
# def sol(str1, str2):
#     start = 0
#     while True:
#         end = len(str1) + start
#         if end > len(str2):
#             return 0
#         tmp, result = search(str1, str2[start:end])
#         # print(tmp, result)
#         start += tmp
#         if result == 1:
#             return 1
#         # print(result)
#
#
# for i, strings in enumerate(data):
#     str1 = strings[0]
#     str2 = strings[1]
#     print("#%s" %(i + 1), sol(str1, str2))
#
# # print(sol("rithm", "a pattern matching algorithm"))
#
#





for t in range(int(input())):
    str1, str2 = input(), input()
    lstr1, lstr2 = len(str1), len(str2)
    sid = lstr1-1
    res =0
    while True:
        check = str2[sid]
        pos = str1.find(check)
        if pos == lstr1-1 or sid == lstr2-1:
            if str2[ sid-lstr1+1:sid+1] == str1:
                res = 1
                break
            else: # 안맞으면?
                if sid == lstr2-1:
                    break
                else:
                    sid +=1
        elif pos == -1:
            sid += lstr1
            if sid >=lstr2:
                sid = lstr2-1
        else:
            sid += lstr1-pos-1
            if sid >=lstr2:
                sid = lstr2-1
    print('#{} {}'.format(t+1,res))

















