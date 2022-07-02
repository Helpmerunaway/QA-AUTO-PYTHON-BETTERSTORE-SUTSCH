import random

lower_eng = "abcdefghijklmnopqrstuvwxyz"
upper_eng = "ABCDEFGHIJKLMNPOQRSTUVWXYZ"
number = "0123456789"
symbols = "[]{}();*/-_"
all_eng = lower_eng + upper_eng + number + symbols
lenght = 10
generated_password_eng = "".join(random.sample(all_eng, lenght))
print(generated_password_eng)

lower_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
upper_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЧШЩЪЫЬЭЮЯ"
all_rus = lower_rus + upper_rus + number + symbols
lenght = 10
generated_password_rus = "".join(random.sample(all_rus, lenght))
print(generated_password_rus)