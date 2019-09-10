from itertools import combinations, permutations

arr = [1, 2, 3, 4, 5]
count = 1
for front_end in combinations(arr, 2):
    perm_candi = [i for i in arr if i not in front_end]
    for middle in permutations(perm_candi, len(perm_candi)):
        new_arr = [front_end[0]] + list(middle) + [front_end[1]]
        print(count, new_arr)
        count += 1
