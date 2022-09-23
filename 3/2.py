#Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3
first_value = float(input("Введите первое число: "))
second_value = float(input("Введите второе число: "))
third_value = float(input("Введите третье число: "))
arif_summ = (first_value+second_value+third_value)/3
print("Арифметическая сумма равна:", round(arif_summ, 3))


