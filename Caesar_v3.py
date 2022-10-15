'''

Реализовать шифр Цезаря с тремя параметрами на вход: фраза для шифрования (строка), сдвиг (число), алфавит (rus/eng). Реализовать зашифровку encrypt() и расшифровку decrypt().

'''

rus1 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' # русский с буквой ё
rus2 = 'абвгдежзийклмнопрстуфхцчшщъыьэюя' # русский без буквы ё
eng = 'abcdefghijklmnopqrstuvwxyz' # английский

# Дополнительная функция, нужная для сохранения пробелов и знаков препинания 
def is_sign(sym):
    signs = ' .,:;?!*&%+=-_@#\'\"'
    counter = 0
    while counter < len(signs):
        if sym == signs[counter]:
            return True
        counter += 1
    return False

# phrase - исходный текст
# rot - сдвиг (на сколько букв надо сдвинуть вправо по алфавиту)
# # alphabet - выбор нужного алфавита (русский с ё или без, английский, можно добавить любой язык в начало документа перед функциями)

# функция для зашифровки:

def caesar_encrypt(phrase, rot, alphabet):
    result = ''
    alphabet = alphabet
    for i in phrase:
        if is_sign(i):
            result += i
        elif i.isupper():
            if (alphabet.find(i.lower()) + rot) >= len(alphabet):
                result += (alphabet[alphabet.find(i.lower()) + rot - len(alphabet)]).upper()
            elif (alphabet.find(i.lower()) + rot) < len(alphabet):
                result += (alphabet[alphabet.find(i.lower()) + rot]).upper()
        elif not i.isupper():
            if (alphabet.find(i.lower()) + rot) >= len(alphabet):
                result += alphabet[alphabet.find(i) + rot - len(alphabet)]
            elif (alphabet.find(i) + rot) < len(alphabet):
                result += alphabet[alphabet.find(i) + rot]
    return result

# функция для расшифровки:
  
def caesar_decrypt(phrase, rot, alphabet):
    result = ''
    alphabet = alphabet
    for i in phrase:
        if is_sign(i):
            result += i
        elif i.isupper():
            if (alphabet.find(i.lower()) - rot) >= len(alphabet):
                result += (alphabet[alphabet.find(i.lower()) - rot - len(alphabet)]).upper()
            elif (alphabet.find(i.lower()) - rot) < len(alphabet):
                result += (alphabet[alphabet.find(i.lower()) - rot]).upper()
        elif not i.isupper():
            if (alphabet.find(i.lower()) - rot) >= len(alphabet):
                result += alphabet[alphabet.find(i) - rot - len(alphabet)]
            elif (alphabet.find(i) - rot) < len(alphabet):
                result += alphabet[alphabet.find(i) - rot]
    return result



#print(caesar_encrypt('Привет, каК дела?', 18, rus1))
#print(caesar_encrypt('Hey, what\'s uP?', 18, eng))

#print(caesar_decrypt('Бвъуцд, ьсЬ хцэс?', 18, rus1))
#print(caesar_decrypt('Zwq, ozsl\'k mH?', 18, eng))
#print(caesar_decrypt('Ifz, xibu\'t vQ?', 1, eng))