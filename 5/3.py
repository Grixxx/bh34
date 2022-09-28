# Вывести четные числа от 2 до N по 5 в строку
i = 0
num = 2
Range = int(input())
while i!= Range:
 if i % 6 == 0:
    print()
    i+=1
 elif num % 2 == 0:
    print(num, end=' ')
    i += 1
 num += 1
