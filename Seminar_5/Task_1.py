# Напишите программу, удаляющую из текста все слова, содержащие абв


text = input ('Введите текст: ')
  
def delet_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = delet_words(text)
print(my_text)