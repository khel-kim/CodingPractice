def sum_two_arrays(arr1, arr2):
    new_arr = []
    for i in range(len(arr1)):
        new_arr.append(arr1[i] | arr2[i])
    return new_arr


def convert_array_to_map(arr):
    board = []
    for i in arr:
        string = str(bin(i))[2:].rjust(len(arr), "0")
        board.append("".join((map(lambda x: "#" if x == '1' else " ", string))))
    return board


def solution(n, arr1, arr2):
    return convert_array_to_map(sum_two_arrays(arr1, arr2))