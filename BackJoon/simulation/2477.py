k = int(input())
lines = []
even_lines = []
odd_lines = []
for i in range(6):
    tmp = list(map(int, input().split()))
    if i & 1 == 0: even_lines.append(tmp[1])
    else: odd_lines.append(tmp[1])
    lines.append(tmp)
normal = [4, 2, 3, 1]
height = max(even_lines)
width = max(odd_lines)

start_index = normal.index(lines[0][0])
corner = start_index
for i in range(1, 6):
    corner = (corner + 1) % 4
    if normal[corner] != lines[i][0]:
        corner = i
        break
else:
    corner = 0
before_corner = (corner - 1) % 6
except_area = lines[before_corner][1] * lines[corner][1]

print((height * width - except_area) * k)
