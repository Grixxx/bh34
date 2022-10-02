def shift(n):
    i = 0
    lst = [1, 2, 3, 4, 5]
    while i < n:
      lst = lst[-1:]+lst[:-1]
      i = i+1
    return lst
print(shift(3))