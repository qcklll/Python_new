txt = input("Введите текст: ")
txt = txt.lower()

words = txt.split(" ")

longest_word = ""
shortest_word = ""
new_text = ""

for word in words:
    word = word.strip(".,:;-!?")  # Удаляем знаки пунктуации с обоих концов слова
    if len(word) > len(longest_word):
        longest_word = word
    if len(word) < len(shortest_word) or not shortest_word:
        shortest_word = word

for word in words:
    if word.strip(".,:;-!?") not in [longest_word, shortest_word]:
        new_text += word + " "

print(new_text.strip())  # Удаляем лишний пробел в конце и выводим новый текст

        

        
