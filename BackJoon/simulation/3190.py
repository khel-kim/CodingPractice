from collections import deque

n = int(input())
k = int(input())
apples = []
for _ in range(k):
    apple = list(map(int, input().split()))
    apples.append([apple[0] - 1, apple[1] - 1, 0])
x = int(input())
moves = deque()
for _ in range(x):
    tmp = input().split()
    time, move = int(tmp[0]), tmp[1]
    moves.append((time, move))


class Snack:
    def __init__(self, direction="right"):
        self.direction = direction
        self.body = deque([[0, 0]])
        self.alive = True
        self.full = False

    def crush(self, current_location):
        if list(current_location) in list(self.body)[:-1]:
            self.alive = False
        else:
            if not 0 <= current_location[0] < n:
                self.alive = False
            elif not 0 <= current_location[1] < n:
                self.alive = False

    def move_head(self):
        if self.direction == "up":
            self.body.append([self.body[-1][0] - 1, self.body[-1][1]])
        elif self.direction == "right":
            self.body.append([self.body[-1][0], self.body[-1][1] + 1])
        elif self.direction == "down":
            self.body.append([self.body[-1][0] + 1, self.body[-1][1]])
        else:
            self.body.append([self.body[-1][0], self.body[-1][1] - 1])

    def move_tail(self):
        if self.full is False:
            self.body.popleft()

    def eat(self):
        top = list(self.body[-1])
        top.append(0)
        try:
            eaten_apple_index = apples.index(top)
            apples[eaten_apple_index][2] = 1
            self.full = True
        except ValueError:
            self.full = False

    def change_direction(self, toward_direct):
        if toward_direct == "D":
            if self.direction == "up":
                return "right"
            elif self.direction == "right":
                return "down"
            elif self.direction == "down":
                return "left"
            else:  # self.direction == "left"
                return "up"
        elif toward_direct == "L":
            if self.direction == "up":
                return "left"
            elif self.direction == "right":
                return "up"
            elif self.direction == "down":
                return "right"
            else:  # self.direction == "left"
                return "down"
        else:
            return self.direction


snack = Snack()
step = 1
directions = []
change_move = moves.popleft()
while True:
    step += 1
    until_time, toward_direction = change_move
    if step & 1 == 0:
        snack.move_head()
        snack.crush(snack.body[-1])
        if snack.alive is False:
            break
        snack.eat()
    else:
        snack.move_tail()

    if step // 2 == until_time:
        snack.direction = snack.change_direction(toward_direction)
        if moves:
            change_move = moves.popleft()
        else:
            change_move = [-1, "S"]

print(step // 2)
