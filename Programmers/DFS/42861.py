def solution(n, costs):
    edges = {i: [] for i in range(n)}
    for x, y, cost in costs:
        edges[x].append((y, cost))
        edges[y].append((x, cost))

    check_list = [False] * n
    check_list[0] = True
    visit = [0]
    count = 0
    for _ in range(n-1):
        min_value = 999999
        min_node = None
        for key in visit:
            new_edge = []
            for node, value in edges[key]:
                if check_list[node]: continue
                new_edge.append((node, value))
                if min_value > value:
                    min_value = value
                    min_node = node
            edges[key] = new_edge

        check_list[min_node] = True
        visit.append(min_node)
        count += min_value
    return count