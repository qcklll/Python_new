txt = input("Введите зашифрованный текст: ")

non_secret = ""

mal_a = ord("а")
big_a = ord("А")
mal_ya = ord("я")
big_ya = ord("Я")
for k in txt:
    s = ord(k)
    if s == mal_ya:
       s = mal_a
    elif s == big_ya:
        s = big_a
    else:
        s += 1

    non_secret_char = chr(s)
    non_secret += non_secret_char

print("Расшифрованный текст: ", non_secret)
        
"""
encrypted_text = input("Введите зашифрованный текст: ")

decrypted_text = ""
for char in encrypted_text:
    ascii_code = ord(char)
    if char.islower() and char != 'z':
        decrypted_char = chr(ascii_code + 1)
    elif char.isupper() and char != 'Z':
        decrypted_char = chr(ascii_code + 1)
    else:
        decrypted_char = chr(ascii_code - 25)  # Замена последней буквы алфавита на первую

    decrypted_text += decrypted_char

print("Расшифрованный текст:", decrypted_text)

"""
