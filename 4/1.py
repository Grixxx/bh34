# Заполнить список степенями числа 2 (от 2^1 до 2^n).
n = int(input())
numbers = [2**i for i in range(n)]
print(numbers)
