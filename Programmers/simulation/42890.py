def solution(relation):
    def combinations(arr, k, visit=[]):
        if check_visit_in_key(visit, candi_keys):
            return
        if len(visit) == k:
            yield visit
        else:
            for i in range(len(arr)):
                visit.append(arr[i])
                yield from combinations(arr[i + 1:], k, visit)
                visit.pop()

    def check_key(key):
        dic = {}
        for index in range(n_rows):
            keys = []
            for candidate_key in key:
                keys.append(relation[index][candidate_key])
            keys = tuple(keys)
            if dic.get(keys):
                dic[keys] += 1
                return False
            else:
                dic[keys] = 1
        return True

    def check_visit_in_key(visit, keys):
        if not keys or not visit:
            return False
        for k in keys:
            if check_include(k, visit):
                return True
        return False

    def check_include(set1, set2):
        for i in set1:
            if i in set2:
                pass
            else:
                return False
        else:
            return True

    n_rows = len(relation)
    n_columns = len(relation[0])
    column = [i for i in range(n_columns)]
    candi_keys = []
    for n_key in range(1, n_columns+1):
        for candi in combinations(column, n_key):
            if check_key(candi):
                candi_keys.append(candi.copy())
    return len(candi_keys)
