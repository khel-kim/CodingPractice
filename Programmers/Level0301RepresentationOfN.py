def solution(N, number):
    if N == number:
        return 1
    else:
        n = str(N)
        number_str = str(number)

        operations1 = ["+", "*"]
        operations2 = ["-", "//"]

        memo = [n]
        queue = [n]
        count = 2
        last = n
        while queue:
            current = queue.pop(0)
            for operation in operations1:
                tmp = str(eval(current + operation + n))
                if tmp not in memo:
                    memo.append(tmp)
                    queue.append(tmp)
            for operation in operations2:
                tmp1 = str(eval(current + operation + n))
                if tmp1 not in memo:
                    memo.append(tmp1)
                    queue.append(tmp1)
                if current != "0":
                    tmp2 = str(eval(n + operation + current))
                    if tmp2 not in memo:
                        memo.append(tmp2)
                        queue.append(tmp2)
            if last == current:
                memo.append(n * count)
                queue.append(n * count)
                if number_str in queue:
                    break
                count += 1
                last = queue[-1]
            if count >= 8:
                return -1
    return count


print(solution(2, 22))
