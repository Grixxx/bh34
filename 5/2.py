# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число
import os
while True:
 first_num = int(input("Введите первое число: "))
 sign = input("Введите один из знаков (+, -, *, /) : ")
 second_nam = int(input("Введите второе число: "))
 if sign in ('+', '-', '*', '/'):
     if  sign == '+':
         print(first_num + second_nam)
     elif  sign == '-':
         print(first_num -second_nam)
     elif  sign == '*':
         print(first_num*second_nam)
     elif  sign == '/':
        if second_nam == 0:
             print("Делить на ноль нельзя")
        else:
             print(first_num/second_nam)
     else:
         print("Вы ввели неверный знак")
 os.system('cls')



