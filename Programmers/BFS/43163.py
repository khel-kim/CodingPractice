from collections import deque


def solution(begin, target, words):
    def get_difference(w1, w2):
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
            if count > 1:
                return False
        return True

    def bfs():
        queue = deque([(begin, 0)])
        check_list = [False] * len(words)
        while queue:
            current_word, depth = queue.popleft()
            for i, word in enumerate(words):
                if check_list[i] is False and get_difference(current_word, word):
                    if word == target:
                        return depth+1
                    else:
                        check_list[i] = True
                        queue.append((word, depth+1))
        return 0

    return bfs()
