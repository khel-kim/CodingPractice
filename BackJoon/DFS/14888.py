import itertools
permutation = itertools.permutations

n = int(input())
numbers = list(map(int, input().split()))
n_operations = list(map(int, input().split()))

operations = "+" * n_operations[0] + "-" * n_operations[1] + "*" * n_operations[2] + "/" * n_operations[3]


def operate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num1 < 0:
            return -(-num1 // num2)
        else:
            return num1 // num2


maximum = -1000000000
minimum = 1000000000
for operation in permutation(operations, n-1):
    current_num = numbers[0]
    for i in range(0, n-1):
        current_num = operate(current_num, numbers[i+1], operation[i])
    if maximum < current_num:
        maximum = current_num
    if minimum > current_num:
        minimum = current_num

print(maximum)
print(minimum)
