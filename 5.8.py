vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']  # Гласные буквы
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']  # Согласные буквы

txt = input("Введите текст: ")
txt = txt.lower()
characters = list(txt)
for k in range(len(characters)) :
    if characters[k] in vowels:
        vowel_index = vowels.index(characters[k])
        if vowel_index == len(vowels) - 1:
            characters[k] = vowels[0]
        else:
            characters[k] = vowels[vowel_index + 1]
        
        
for k in range(len(characters)) :
    if characters[k] in consonants:
        conso_index = consonants.index(characters[k])
        if conso_index == len(consonants) - 1:
            characters[k] = consonants[0]
        else:
            characters[k] = consonants[conso_index + 1]

print("Измененный текст:", "".join(characters))        
        
    
    
    
