import sys
sys.setrecursionlimit(10 ** 9)


def solution(nodeinfo):
    nodes_dic = {}
    levels_dic = {}
    max_y = 0
    for i, (x, y) in enumerate(nodeinfo):
        nodes_dic[(x, y)] = i + 1
        if levels_dic.get(y) is not None:
            levels_dic[y].append(x)
        else:
            levels_dic[y] = [x]
        if max_y < y:
            max_y = y
    levels = [i for i in range(max_y, -1, -1)]
    heap = {}
    for y in levels:
        for x in levels_dic.get(y, []):
            heap_index = 1
            while heap.get(heap_index) is not None:
                if heap[heap_index][0] > x:
                    heap_index = heap_index * 2
                else:
                    heap_index = heap_index * 2 + 1
            heap[heap_index] = (x, y)

    def pre_order(index):
        if heap.get(index) is not None:
            visit1.append(nodes_dic[heap[index]])
            pre_order(2 * index)
            pre_order(2 * index + 1)

    def post_order(index):
        if heap.get(index) is not None:
            post_order(2 * index)
            post_order(2 * index + 1)
            visit2.append(nodes_dic[heap[index]])

    visit1 = []
    visit2 = []
    pre_order(1)
    post_order(1)
    return [visit1, visit2]
