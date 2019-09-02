def solution(routes):
    routes.sort(key=lambda x: x[1])
    check_point= -30000
    end_list = []
    for start, end in routes:
        if check_point < start:
            end_list.append(end)
            check_point = end
    return len(end_list)
