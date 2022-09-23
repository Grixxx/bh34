# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
sentence = input()
sep = sentence.replace(' ', '-')
print(sep)     # 1 способ
print("-----------------------------------------------------------------------------")
sentenceNum = input()
c = sentenceNum.split(' ')
sentenceNum = '-'.join(c)
print(sentenceNum)      # 2 способ




