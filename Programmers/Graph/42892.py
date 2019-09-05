nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
node_with_index = {(x, y): i+1 for i, (x, y) in enumerate(nodeinfo)}

dic = {}
for x, y in nodeinfo:
    if dic.get(y):
        dic[y].append(x)
    else:
        dic[y] = [x]
levels = sorted(list(dic.keys()), reverse=True)


print("nodes", node_with_index)
print("levels", levels)
print(dic)

heap = [0] * (2 ** len(levels) + 1)
heap[1] = node_with_index[(dic[levels[0]][0], levels[0])]
print(heap)
start = 1
for level in levels[1:]:
    end = 2 ** start
    level_list = sorted(dic[level])
    prev_level_list = heap[start:end]
    print(prev_level_list)
    print(level_list)
    for i in range(start, end):
        now = heap[i]





