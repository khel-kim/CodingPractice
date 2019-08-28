dic = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    3: [7, 8],
    # 4: [],
    # 5: [],
    # 6: [],
    # 7: [],
    # 8: [],
}


# def recursion(current):
#     if dic.get(current):
#         recursion(dic[current][0])
#         recursion(dic[current][1])
#         print(current)
#
#
# recursion(0)



def recursion(current):
    # print(current)
    # print(visit)
    if dic.get(current):
        for i in dic[current]:
            visit.append(i)
            recursion(i)
            visit.pop()

        # visit.append(dic[current][1])
        # recursion(dic[current][1])
        # visit.pop()
        #
        # visit.append(dic[current][2])
        # recursion(dic[current][2])
        # visit.pop()


    else:
        print(visit)

visit = [0] # 시작 위치
print(recursion(0))








dic = {
    0: [1, 2, 3],
    1: [4, 5, 6],
    2: [7, 8, 9],
    3: [10, 11, 12],
}