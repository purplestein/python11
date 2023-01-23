from chardet import detect


def encoding_convert():
    with open('test_file.txt', 'rb') as f_obj:
        content_bytes = f_obj.read()
    detected = detect(content_bytes)
    print(detected)
    encoding = detected['encoding']
    content_text = content_bytes.decode()
    with open('test_file.txt', 'w', encoding='utf-8') as f_obj:
        f_obj.write(content_text)


encoding_convert()
