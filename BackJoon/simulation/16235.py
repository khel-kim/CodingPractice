# x, y, age를 리스트로 관리하는 것보다 tuple로 관리하는 것이 빠름
# 아마 unpack을 할 때 튜플로 하는게 더 빠른듯
from collections import deque

n, m, k = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
trees = deque([])
for _ in range(m):
    tmp = list(map(int, input().split()))
    trees.append((tmp[0] - 1, tmp[1] - 1, tmp[2]))

reproduction = ((0, 1), (1, 0), (0, -1), (-1, 0),
                (1, 1), (1, -1), (-1, -1), (-1, 1))


a = [[5] * n for _ in range(n)]
depth_trees = [[0] * n for _ in range(n)]


def spring():
    global alive_trees, reproductive_trees, trees
    alive_trees = deque([])
    reproductive_trees = []
    for tree in trees:
        x, y, age = tree
        if a[x][y] < age:
            depth_trees[x][y] += age // 2
        else:
            a[x][y] -= age
            age += 1
            alive_trees.append((x, y, age))
            if age % 5 == 0:
                reproductive_trees.append((x, y, age))
    trees = alive_trees


def fall():
    for tree in reproductive_trees:
        x, y, age = tree
        for dx, dy in reproduction:
            nx = x + dx
            ny = y + dy
            if nx < 0: continue
            if nx >= n: continue
            if ny < 0: continue
            if ny >= n: continue
            alive_trees.appendleft((nx, ny, 1))


def winter():
    for i in range(n):
        for j in range(n):
            a[i][j] += A[i][j] + depth_trees[i][j]
            depth_trees[i][j] = 0


for __ in range(k):
    spring()
    if len(trees) == 0:
        break
    fall()
    winter()
print(len(trees))
