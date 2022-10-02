#Дан список содержащий в себе различные типы данных, отфильтровать таким образом, чтобы остались только строки, использование дополнительного списка незаконно
list_my = [1, 'hello', True, 'fsfsf' ]
list_my = map(str, list_my)
result = list(filter(lambda x: x.isalpha(), list_my))
print(result)
