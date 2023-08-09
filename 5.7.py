txt = input("Введите текст: ")


decrypted_text = ""

for char in txt:
    ascii_code = ord(char)
    if char.islower() and char == "б":
        decrypted_char = chr(ascii_code + 30) 
    elif char.isupper() and char == "Б":
        decrypted_char = chr(ascii_code + 30)
    elif char.islower() and char == "а":
        decrypted_char = chr(ascii_code + 30)
    elif char.isupper() and char == "А":
        decrypted_char = chr(ascii_code + 30)
    else:
        decrypted_char = chr(ascii_code - 2)

    decrypted_text += decrypted_char

print("Зашифрованный текст:", decrypted_text)

encrypted_text = ""

for char in decrypted_text:
    ascii_code = ord(char)
    if char.islower() and char == "я":
        decrypted_char = chr(ascii_code - 30) 
    elif char.isupper() and char == "Я":
        decrypted_char = chr(ascii_code - 30)
    elif char.islower() and char == "ю":
        decrypted_char = chr(ascii_code - 30)
    elif char.isupper() and char == "Ю":
        decrypted_char = chr(ascii_code - 30)
    else:
        decrypted_char = chr(ascii_code + 2)

    encrypted_text += decrypted_char

print("Расшифрованный текст:", encrypted_text)
