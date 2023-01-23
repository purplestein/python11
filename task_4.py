my_lst = ['разработка', 'администрирование', 'protocol', 'standart']

for el in my_lst:
    a = el.encode('utf-8')
    print(a, type(a))
    b = bytes.decode(a, 'utf-8')
    print(b, type(b))