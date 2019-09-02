def solution(n, edge):
    from collections import deque
    edges = {i: [] for i in range(1, n+1)}
    depth_dic = {i: 0 for i in range(0, n)}
    check = [False] * (n + 1)
    for node1, node2 in edge:
        edges[node1].append(node2)
        edges[node2].append(node1)

    queue = deque([(1, 0)])
    check[1] = True
    depth_dic[0] += 1
    while queue:
        key, depth = queue.popleft()
        for node in edges[key]:
            if check[node]: continue
            check[node] = True
            queue.append((node, depth+1))
            depth_dic[depth+1] += 1
    return depth_dic[depth]