i = 0
number = 0
amount = int(input("ведите количество чисел: "))
multiplicity= int(input("Введите число для кратности: "))
K = int(input("Введите число K: "))
while i !=amount:
  if number % multiplicity == 0 and number > K:
    print(number)
    i += 1
  number += 1