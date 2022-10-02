numbers = [3, 2, 5, 6, 7, 8, 1]
numbers_1 = list(filter(lambda x: not x%2, numbers))
numbers_2 = list(filter(lambda x: x%2, numbers))
print(numbers_1)
print(numbers_2)