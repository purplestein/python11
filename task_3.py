B_word = ['attribute', 'type', 'функция', 'класс']
for el in B_word:
    if el.isascii() is True:
        print(type(el))
    else:
        print("Ошибка! Только латинские символы!")

a = input("Введите символы - b'символы':")

try:
    print(type(eval(a)))
except SyntaxError as exc:
    print("Ошибка! Только латинские символы!")
