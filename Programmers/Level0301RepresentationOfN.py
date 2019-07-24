def solution(n, number):
    if n == number:
        return 1
    memo = [[], [n]]
    duplicated = [n]
    while True:
        if len(memo) > 8:
            return -1
        else:
            current = []
            for i in range(1, len(memo)):
                check_list1 = memo[i]
                for j in range(1, len(memo)):
                    check_list2 = memo[j]
                    if i + j == len(memo) and i >= j:
                        for num1 in check_list1:
                            for num2 in check_list2:
                                if num1 + num2 not in duplicated and num1 + num2 not in current:
                                    current.append(num1 + num2)
                                if num1 * num2 not in duplicated and num1 * num2 not in current:
                                    current.append(num1 * num2)

                                if num1 - num2 not in duplicated and num1 - num2 not in current:
                                    current.append(num1 - num2)
                                if num2 - num1 not in duplicated and num2 - num1 not in current:
                                    current.append(num2 - num1)

                                if num2 != 0:
                                    if num1 // num2 not in duplicated and num1 // num2 not in current:
                                        current.append(num1 // num2)
                                if num1 != 0:
                                    if num2 // num1 not in duplicated and num2 // num1 not in current:
                                        current.append(num2 // num1)

            str_n = str(n)
            if int(str_n * len(memo)) not in duplicated and int(str_n * len(memo)) not in current:
                current.append(int(str_n * len(memo)))
            if number in current:
                return len(memo)
            memo.append(current)
            duplicated.extend(current)


print(solution(5, 26))
