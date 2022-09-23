#Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
first_value = int(input("Введите первое число: "))
second_value = int(input("Введите второе число: "))
third_value = int(input("Введите третье число: "))
print("Количество положительных чисел:",(first_value > 0)+(second_value > 0) + (third_value > 0), " Количество отрицательных: ", (first_value < 0)+(second_value < 0) + (third_value < 0))
